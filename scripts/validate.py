#!/usr/bin/env python3
"""Validate and mechanically inspect the canonical Minitongue repository.

Dependency-free checks cover file shape, IDs, references, JSON-in-TSV,
Unicode NFC, bare IPA storage, and mechanically checkable Leipzig alignment.
Discovery modes expose repository facts that should be obtained mechanically
rather than rediscovered by inspection or model inference. If the optional
`jsonschema` package is installed, schema.json is also checked against its
declared meta-schema.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

GRAMMAR_FILE = "grammar.md"
LEXICON_FILE = "lexicon.tsv"
EXAMPLES_FILE = "examples.tsv"
SCHEMA_FILE = "schema.json"

LEXICON_HEADER = [
    "lexeme_id", "lemma", "ipa", "pos", "features", "etymology",
    "sense_id", "definition", "usage", "notes",
]
EXAMPLES_HEADER = [
    "example_id", "judgment", "text", "ipa", "segmentation", "gloss",
    "translation", "rule_refs", "violated_rule_refs", "lexeme_refs", "notes",
]

RULE_RE = re.compile(r"^G-(PHON|ORTH|MORPH|SYN|SEM|PRAG|DISC|LEX)-[0-9]{3,}$")
LEXEME_RE = re.compile(r"^L-[0-9]{4,}$")
SENSE_RE = re.compile(r"^(L-[0-9]{4,})-S[0-9]{2,}$")
EXAMPLE_RE = re.compile(r"^EX-[0-9]{4,}$")
POS_RE = re.compile(r"^[a-z][a-z0-9_-]*$")
RULE_HEADING_RE = re.compile(
    r"^###\s+(G-(?:PHON|ORTH|MORPH|SYN|SEM|PRAG|DISC|LEX)-[0-9]{3,})\s+[—–-]\s+(.+?)\s*$"
)

# Appendix to the Leipzig Glossing Rules (official standard abbreviations).
LEIPZIG_ABBREVIATIONS = {
    "1", "2", "3", "A", "ABL", "ABS", "ACC", "ADJ", "ADV", "AGR", "ALL",
    "ANTIP", "APPL", "ART", "AUX", "BEN", "CAUS", "CLF", "COM", "COMP",
    "COMPL", "COND", "COP", "CVB", "DAT", "DECL", "DEF", "DEM", "DET",
    "DIST", "DISTR", "DU", "DUR", "ERG", "EXCL", "F", "FOC", "FUT", "GEN",
    "IMP", "INCL", "IND", "INDF", "INF", "INS", "INTR", "IPFV", "IRR", "LOC",
    "M", "N", "NEG", "NMLZ", "NOM", "OBJ", "OBL", "P", "PASS", "PFV", "PL",
    "POSS", "PRED", "PRF", "PRS", "PROG", "PROH", "PROX", "PST", "PTCP",
    "PURP", "Q", "QUOT", "RECP", "REFL", "REL", "RES", "S", "SBJ", "SBJV",
    "SG", "TOP", "TR", "VOC",
}

REQUIRED_METADATA = {"language_name", "language_tag", "metalanguage", "project_version", "status"}


@dataclass
class Report:
    errors: list[str]
    warnings: list[str]

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def read_utf8(path: Path, report: Report) -> str:
    try:
        raw = path.read_bytes()
    except FileNotFoundError:
        report.error(f"missing required file: {path}")
        return ""
    if raw.startswith(b"\xef\xbb\xbf"):
        report.error(f"{path}: UTF-8 BOM is not allowed")
    try:
        text = raw.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        report.error(f"{path}: not valid UTF-8 ({exc})")
        return ""
    if unicodedata.normalize("NFC", text) != text:
        report.error(f"{path}: text is not Unicode NFC-normalized")
    return text


def strip_nonsemantic_markdown(text: str) -> str:
    """Remove HTML comments and fenced code so examples/templates are not parsed as data."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    out: list[str] = []
    in_fence = False
    fence_char = ""
    for line in text.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence = True
                fence_char = marker
            elif marker == fence_char:
                in_fence = False
                fence_char = ""
            continue
        if not in_fence:
            out.append(line)
    return "\n".join(out)


def markdown_section(text: str, heading: str, level: int = 3) -> str:
    lines = text.splitlines()
    prefix = "#" * level + " "
    start = None
    for i, line in enumerate(lines):
        if line.strip() == prefix + heading:
            start = i + 1
            break
    if start is None:
        return ""
    end = len(lines)
    for j in range(start, len(lines)):
        if re.match(rf"^#{{1,{level}}}\s+", lines[j]):
            end = j
            break
    return "\n".join(lines[start:end])


def parse_markdown_table(section: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in section.splitlines():
        s = line.strip()
        if not (s.startswith("|") and s.endswith("|")):
            continue
        cells = [c.strip() for c in s[1:-1].split("|")]
        if cells and all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
            continue
        rows.append(cells)
    return rows


def parse_grammar(path: Path, report: Report) -> tuple[set[str], set[str], set[str]]:
    text = read_utf8(path, report)
    clean = strip_nonsemantic_markdown(text)

    metadata_rows = parse_markdown_table(markdown_section(clean, "Metadata", level=2))
    metadata: dict[str, str] = {}
    if metadata_rows and [c.lower() for c in metadata_rows[0]] == ["key", "value"]:
        for row in metadata_rows[1:]:
            if len(row) == 2 and row[0]:
                metadata[row[0]] = row[1]
    missing_meta = REQUIRED_METADATA - metadata.keys()
    if missing_meta:
        report.error(f"{path}: missing metadata keys: {', '.join(sorted(missing_meta))}")

    rules: set[str] = set()
    for lineno, line in enumerate(clean.splitlines(), 1):
        match = RULE_HEADING_RE.match(line)
        if match:
            rule_id = match.group(1)
            if rule_id in rules:
                report.error(f"{path}:{lineno}: duplicate rule id {rule_id}")
            rules.add(rule_id)

    pos_rows = parse_markdown_table(markdown_section(clean, "Parts of speech", level=3))
    pos_codes: set[str] = set()
    if pos_rows:
        if [c.lower() for c in pos_rows[0]] != ["code", "name", "notes"]:
            report.error(f"{path}: Parts of speech table must use columns: Code | Name | Notes")
        for row in pos_rows[1:]:
            if len(row) != 3 or not row[0]:
                continue
            code = row[0]
            if not POS_RE.fullmatch(code):
                report.error(f"{path}: invalid POS code {code!r}")
            if code in pos_codes:
                report.error(f"{path}: duplicate POS code {code!r}")
            pos_codes.add(code)

    abbr_rows = parse_markdown_table(markdown_section(clean, "Project-specific gloss abbreviations", level=3))
    custom_abbr: set[str] = set()
    if abbr_rows:
        if [c.lower() for c in abbr_rows[0]] != ["abbreviation", "meaning", "notes"]:
            report.error(
                f"{path}: Project-specific gloss abbreviations table must use columns: Abbreviation | Meaning | Notes"
            )
        for row in abbr_rows[1:]:
            if len(row) != 3 or not row[0]:
                continue
            abbr = row[0]
            if not re.fullmatch(r"[A-Z0-9][A-Z0-9.-]*", abbr):
                report.error(f"{path}: invalid gloss abbreviation {abbr!r}")
            if abbr in custom_abbr:
                report.error(f"{path}: duplicate gloss abbreviation {abbr!r}")
            custom_abbr.add(abbr)

    return rules, pos_codes, custom_abbr


def read_tsv(path: Path, expected_header: list[str], report: Report) -> list[dict[str, str]]:
    text = read_utf8(path, report)
    if not text:
        return []
    reader = csv.reader(text.splitlines(), delimiter="\t", quoting=csv.QUOTE_MINIMAL)
    rows = list(reader)
    if not rows:
        report.error(f"{path}: empty file")
        return []
    if rows[0] != expected_header:
        report.error(
            f"{path}: wrong header\n  expected: {' | '.join(expected_header)}\n  found:    {' | '.join(rows[0])}"
        )
        return []
    result: list[dict[str, str]] = []
    for lineno, row in enumerate(rows[1:], 2):
        if not row or all(cell == "" for cell in row):
            report.warn(f"{path}:{lineno}: blank row ignored")
            continue
        if len(row) != len(expected_header):
            report.error(f"{path}:{lineno}: expected {len(expected_header)} columns, found {len(row)}")
            continue
        if any("\n" in cell or "\r" in cell or "\t" in cell for cell in row):
            report.error(f"{path}:{lineno}: embedded tab/newline in field is not allowed")
        record = dict(zip(expected_header, row))
        record["__line__"] = str(lineno)
        result.append(record)
    return result


def require_fields(path: Path, row: dict[str, str], fields: Iterable[str], report: Report) -> None:
    lineno = row["__line__"]
    for field in fields:
        if not row[field].strip():
            report.error(f"{path}:{lineno}: required field {field!r} is empty")


def check_bare_ipa(path: Path, lineno: str, value: str, report: Report) -> None:
    if any(ch in value for ch in "/[]"):
        report.error(f"{path}:{lineno}: IPA must be stored bare (no /.../ or [...] delimiters): {value!r}")
    if value != value.strip():
        report.error(f"{path}:{lineno}: IPA has leading/trailing whitespace")
    if unicodedata.normalize("NFC", value) != value:
        report.error(f"{path}:{lineno}: IPA is not NFC-normalized")


def parse_json_object(path: Path, lineno: str, field: str, value: str, report: Report) -> dict:
    try:
        obj = json.loads(value)
    except json.JSONDecodeError as exc:
        report.error(f"{path}:{lineno}: {field} is invalid JSON ({exc.msg})")
        return {}
    if not isinstance(obj, dict):
        report.error(f"{path}:{lineno}: {field} must be a JSON object")
        return {}
    return obj


def validate_lexicon(path: Path, pos_codes: set[str], report: Report) -> tuple[set[str], set[str], int]:
    rows = read_tsv(path, LEXICON_HEADER, report)
    lexeme_ids: set[str] = set()
    sense_ids: set[str] = set()
    signatures: dict[str, tuple[str, str, str, str, str]] = {}

    for row in rows:
        line = row["__line__"]
        require_fields(path, row, ["lexeme_id", "lemma", "ipa", "pos", "features", "sense_id", "definition"], report)
        lexeme_id = row["lexeme_id"]
        sense_id = row["sense_id"]

        if lexeme_id and not LEXEME_RE.fullmatch(lexeme_id):
            report.error(f"{path}:{line}: invalid lexeme_id {lexeme_id!r}")
        if sense_id:
            m = SENSE_RE.fullmatch(sense_id)
            if not m:
                report.error(f"{path}:{line}: invalid sense_id {sense_id!r}")
            elif m.group(1) != lexeme_id:
                report.error(f"{path}:{line}: sense_id {sense_id!r} does not belong to {lexeme_id!r}")

        if sense_id in sense_ids:
            report.error(f"{path}:{line}: duplicate sense_id {sense_id}")
        if sense_id:
            sense_ids.add(sense_id)
        if lexeme_id:
            lexeme_ids.add(lexeme_id)

        if row["ipa"]:
            check_bare_ipa(path, line, row["ipa"], report)
        features = parse_json_object(path, line, "features", row["features"] or "{}", report)
        features_canonical = json.dumps(features, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

        if row["pos"]:
            if not POS_RE.fullmatch(row["pos"]):
                report.error(f"{path}:{line}: invalid POS code {row['pos']!r}")
            elif not pos_codes:
                report.error(f"{path}:{line}: grammar.md has no declared POS codes; add {row['pos']!r} to Parts of speech")
            elif row["pos"] not in pos_codes:
                report.error(f"{path}:{line}: POS code {row['pos']!r} is not declared in grammar.md")

        signature = (row["lemma"], row["ipa"], row["pos"], features_canonical, row["etymology"])
        if lexeme_id in signatures and signatures[lexeme_id] != signature:
            report.error(
                f"{path}:{line}: rows for {lexeme_id} disagree on lemma/ipa/pos/features/etymology"
            )
        elif lexeme_id:
            signatures[lexeme_id] = signature

    if not rows:
        report.warn(f"{path}: template contains no lexical senses yet")
    return lexeme_ids, sense_ids, len(rows)


def split_refs(value: str) -> list[str]:
    return value.split() if value.strip() else []


def valid_person_number(token: str) -> bool:
    return bool(re.fullmatch(r"[123](?:SG|PL|DU|NSG)?", token))


def category_tokens(gloss: str) -> set[str]:
    """Extract all-uppercase grammatical-looking atoms from a Leipzig gloss line."""
    tokens: set[str] = set()
    for word in gloss.split():
        # Leipzig separators that can separate gloss atoms. Keep period in the split because
        # one-to-many grammatical categories such as GEN.PL contain two labels.
        for atom in re.split(r"[-.=;:~\\><()\[\]{}]+", word):
            atom = atom.strip("?!,;:'\"“”‘’")
            if not atom:
                continue
            if re.fullmatch(r"[A-Z0-9][A-Z0-9]*", atom) and (atom.isupper() or atom.isdigit()):
                tokens.add(atom)
    return tokens


def check_leipzig(path: Path, row: dict[str, str], allowed_abbr: set[str], report: Report) -> None:
    line = row["__line__"]
    seg_words = row["segmentation"].split()
    gloss_words = row["gloss"].split()
    if len(seg_words) != len(gloss_words):
        report.error(
            f"{path}:{line}: Leipzig alignment mismatch: segmentation has {len(seg_words)} words, gloss has {len(gloss_words)}"
        )
        return

    for i, (seg, gloss) in enumerate(zip(seg_words, gloss_words), 1):
        for marker, name in (("-", "hyphen"), ("=", "clitic ="), ("~", "reduplication ~")):
            if seg.count(marker) != gloss.count(marker):
                report.error(
                    f"{path}:{line}: Leipzig {name} mismatch in word {i}: {seg!r} ↔ {gloss!r}"
                )
        if seg.count("<") != gloss.count("<") or seg.count(">") != gloss.count(">"):
            report.error(
                f"{path}:{line}: Leipzig infix angle-bracket mismatch in word {i}: {seg!r} ↔ {gloss!r}"
            )

    for token in sorted(category_tokens(row["gloss"])):
        if token in allowed_abbr or valid_person_number(token):
            continue
        report.error(
            f"{path}:{line}: undefined uppercase gloss abbreviation {token!r}; use a Leipzig abbreviation or declare it in grammar.md"
        )


def validate_examples(
    path: Path,
    rules: set[str],
    lexeme_ids: set[str],
    custom_abbr: set[str],
    report: Report,
) -> int:
    rows = read_tsv(path, EXAMPLES_HEADER, report)
    seen: set[str] = set()
    allowed_abbr = LEIPZIG_ABBREVIATIONS | custom_abbr

    for row in rows:
        line = row["__line__"]
        require_fields(
            path,
            row,
            ["example_id", "judgment", "text", "ipa", "segmentation", "gloss", "translation", "rule_refs"],
            report,
        )
        ex_id = row["example_id"]
        if ex_id and not EXAMPLE_RE.fullmatch(ex_id):
            report.error(f"{path}:{line}: invalid example_id {ex_id!r}")
        if ex_id in seen:
            report.error(f"{path}:{line}: duplicate example_id {ex_id}")
        if ex_id:
            seen.add(ex_id)

        if row["judgment"] not in {"grammatical", "ungrammatical", "marginal"}:
            report.error(f"{path}:{line}: invalid judgment {row['judgment']!r}")
        if row["judgment"] == "ungrammatical" and not row["violated_rule_refs"].strip():
            report.error(f"{path}:{line}: ungrammatical examples require violated_rule_refs")
        if row["judgment"] != "ungrammatical" and row["violated_rule_refs"].strip():
            report.warn(f"{path}:{line}: violated_rule_refs is normally blank unless judgment=ungrammatical")

        if row["ipa"]:
            check_bare_ipa(path, line, row["ipa"], report)

        for field in ("rule_refs", "violated_rule_refs"):
            for ref in split_refs(row[field]):
                if not RULE_RE.fullmatch(ref):
                    report.error(f"{path}:{line}: malformed rule reference {ref!r} in {field}")
                elif ref not in rules:
                    report.error(f"{path}:{line}: unknown rule reference {ref!r} in {field}")
        for ref in split_refs(row["lexeme_refs"]):
            if not LEXEME_RE.fullmatch(ref):
                report.error(f"{path}:{line}: malformed lexeme reference {ref!r}")
            elif ref not in lexeme_ids:
                report.error(f"{path}:{line}: unknown lexeme reference {ref!r}")

        if row["segmentation"] and row["gloss"]:
            check_leipzig(path, row, allowed_abbr, report)

    if not rows:
        report.warn(f"{path}: template contains no examples yet")
    return len(rows)


def validate_schema(path: Path, report: Report) -> None:
    text = read_utf8(path, report)
    if not text:
        return
    try:
        schema = json.loads(text)
    except json.JSONDecodeError as exc:
        report.error(f"{path}: invalid JSON ({exc})")
        return
    if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
        report.error(f"{path}: $schema must be JSON Schema Draft 2020-12")
    if schema.get("type") != "object":
        report.error(f"{path}: root schema type must be object")
    if "x-tei" not in schema:
        report.error(f"{path}: missing top-level x-tei mapping metadata")

    try:
        import jsonschema  # type: ignore
    except ImportError:
        return
    try:
        cls = jsonschema.validators.validator_for(schema)
        cls.check_schema(schema)
    except Exception as exc:  # jsonschema exposes several exception subclasses across versions
        report.error(f"{path}: JSON Schema meta-validation failed: {exc}")



def read_tsv_unchecked(path: Path, expected_header: list[str]) -> list[dict[str, str]]:
    """Read a validated TSV for discovery/reporting without mutating validation state."""
    text = path.read_text(encoding="utf-8-sig")
    rows = list(csv.reader(text.splitlines(), delimiter="\t", quoting=csv.QUOTE_MINIMAL))
    if not rows or rows[0] != expected_header:
        return []
    return [dict(zip(expected_header, row)) for row in rows[1:] if len(row) == len(expected_header)]


def next_numbered_id(existing: Iterable[str], prefix: str, width: int) -> str:
    numbers: list[int] = []
    pattern = re.compile(rf"^{re.escape(prefix)}([0-9]+)$")
    for value in existing:
        match = pattern.fullmatch(value)
        if match:
            numbers.append(int(match.group(1)))
    return f"{prefix}{(max(numbers, default=0) + 1):0{width}d}"


def unresolved_items(path: Path) -> list[dict[str, object]]:
    """Return explicit UNSPECIFIED occurrences with source location and nearest context."""
    text = path.read_text(encoding="utf-8-sig")
    current_section = ""
    current_rule = ""
    items: list[dict[str, object]] = []

    for lineno, line in enumerate(text.splitlines(), 1):
        rule_match = RULE_HEADING_RE.match(line)
        if rule_match:
            current_rule = rule_match.group(1)
            current_section = rule_match.group(2)
        else:
            heading_match = re.match(r"^(#{2,3})\s+(.+?)\s*$", line)
            if heading_match:
                current_section = heading_match.group(2)
                current_rule = ""

        if "UNSPECIFIED" in line:
            items.append(
                {
                    "line": lineno,
                    "rule_id": current_rule or None,
                    "section": current_section or None,
                    "text": line.strip(),
                }
            )
    return items


def grammar_rule_block(path: Path, rule_id: str) -> str | None:
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    start = None
    for i, line in enumerate(lines):
        match = RULE_HEADING_RE.match(line)
        if match and match.group(1) == rule_id:
            start = i
            break
    if start is None:
        return None

    end = len(lines)
    for i in range(start + 1, len(lines)):
        if re.match(r"^#{1,3}\s+", lines[i]):
            end = i
            break
    return "\n".join(lines[start:end]).rstrip()


def show_record(root: Path, identifier: str) -> dict[str, object] | None:
    """Return the exact canonical record(s) associated with a stable ID."""
    if RULE_RE.fullmatch(identifier):
        block = grammar_rule_block(root / GRAMMAR_FILE, identifier)
        if block is None:
            return None
        return {"kind": "rule", "id": identifier, "source": GRAMMAR_FILE, "text": block}

    if LEXEME_RE.fullmatch(identifier) or SENSE_RE.fullmatch(identifier):
        rows = read_tsv_unchecked(root / LEXICON_FILE, LEXICON_HEADER)
        key = "sense_id" if SENSE_RE.fullmatch(identifier) else "lexeme_id"
        matches = [row for row in rows if row.get(key) == identifier]
        if not matches:
            return None
        return {"kind": "sense" if key == "sense_id" else "lexeme", "id": identifier, "source": LEXICON_FILE, "records": matches}

    if EXAMPLE_RE.fullmatch(identifier):
        rows = read_tsv_unchecked(root / EXAMPLES_FILE, EXAMPLES_HEADER)
        matches = [row for row in rows if row.get("example_id") == identifier]
        if not matches:
            return None
        return {"kind": "example", "id": identifier, "source": EXAMPLES_FILE, "records": matches}

    return None


def collect_summary(
    root: Path,
    rules: set[str],
    pos_codes: set[str],
    custom_abbr: set[str],
) -> dict[str, object]:
    lex_rows = read_tsv_unchecked(root / LEXICON_FILE, LEXICON_HEADER)
    ex_rows = read_tsv_unchecked(root / EXAMPLES_FILE, EXAMPLES_HEADER)

    lexeme_ids = sorted({row["lexeme_id"] for row in lex_rows if row.get("lexeme_id")})
    sense_ids = sorted({row["sense_id"] for row in lex_rows if row.get("sense_id")})
    example_ids = sorted({row["example_id"] for row in ex_rows if row.get("example_id")})

    rule_domains: dict[str, int] = {}
    next_rule_ids: dict[str, str] = {}
    for domain in ("PHON", "ORTH", "MORPH", "SYN", "SEM", "PRAG", "DISC", "LEX"):
        domain_ids = sorted(rule for rule in rules if rule.startswith(f"G-{domain}-"))
        rule_domains[domain] = len(domain_ids)
        next_rule_ids[domain] = next_numbered_id(domain_ids, f"G-{domain}-", 3)

    judgment_counts = {"grammatical": 0, "ungrammatical": 0, "marginal": 0}
    referenced_rules: set[str] = set()
    referenced_lexemes: set[str] = set()
    for row in ex_rows:
        judgment = row.get("judgment", "")
        if judgment in judgment_counts:
            judgment_counts[judgment] += 1
        referenced_rules.update(split_refs(row.get("rule_refs", "")))
        referenced_rules.update(split_refs(row.get("violated_rule_refs", "")))
        referenced_lexemes.update(split_refs(row.get("lexeme_refs", "")))

    unresolved = unresolved_items(root / GRAMMAR_FILE)
    uncovered_rules = sorted(rules - referenced_rules)
    unreferenced_lexemes = sorted(set(lexeme_ids) - referenced_lexemes)
    next_sense_ids = {
        lexeme_id: next_numbered_id(
            (sense_id for sense_id in sense_ids if sense_id.startswith(f"{lexeme_id}-S")),
            f"{lexeme_id}-S",
            2,
        )
        for lexeme_id in lexeme_ids
    }

    return {
        "rules": {
            "total": len(rules),
            "by_domain": rule_domains,
            "with_regression_coverage": len(rules & referenced_rules),
            "without_regression_coverage": len(uncovered_rules),
            "uncovered_rule_ids": uncovered_rules,
        },
        "lexicon": {
            "lexemes": len(lexeme_ids),
            "senses": len(sense_ids),
            "referenced_by_examples": len(set(lexeme_ids) & referenced_lexemes),
            "unreferenced_lexeme_ids": unreferenced_lexemes,
        },
        "examples": {
            "total": len(ex_rows),
            "by_judgment": judgment_counts,
        },
        "inventories": {
            "pos_codes": sorted(pos_codes),
            "project_gloss_abbreviations": sorted(custom_abbr),
        },
        "unresolved": {
            "explicit_occurrences": len(unresolved),
        },
        "next_ids": {
            "lexeme": next_numbered_id(lexeme_ids, "L-", 4),
            "senses": next_sense_ids,
            "example": next_numbered_id(example_ids, "EX-", 4),
            "rules": next_rule_ids,
        },
    }


def print_summary(summary: dict[str, object]) -> None:
    rules = summary["rules"]
    lexicon = summary["lexicon"]
    examples = summary["examples"]
    inventories = summary["inventories"]
    unresolved = summary["unresolved"]
    next_ids = summary["next_ids"]

    print("Repository summary:")
    print(f"  rules: {rules['total']} ({', '.join(f'{k}={v}' for k, v in rules['by_domain'].items())})")
    print(
        f"  regression coverage: {rules['with_regression_coverage']}/{rules['total']} rules; "
        f"{rules['without_regression_coverage']} uncovered"
    )
    print(f"  lexicon: {lexicon['lexemes']} lexemes, {lexicon['senses']} senses")
    print(
        f"  examples: {examples['total']} "
        f"(grammatical={examples['by_judgment']['grammatical']}, "
        f"ungrammatical={examples['by_judgment']['ungrammatical']}, "
        f"marginal={examples['by_judgment']['marginal']})"
    )
    print(f"  explicit UNSPECIFIED occurrences: {unresolved['explicit_occurrences']}")
    print(f"  POS codes: {', '.join(inventories['pos_codes']) or '(none)'}")
    print(
        "  project gloss abbreviations: "
        f"{', '.join(inventories['project_gloss_abbreviations']) or '(none)'}"
    )
    print(f"  next lexeme ID: {next_ids['lexeme']}")
    print(f"  next example ID: {next_ids['example']}")
    print("  next rule IDs: " + ", ".join(next_ids["rules"].values()))


def print_unresolved(items: list[dict[str, object]]) -> None:
    if not items:
        print("No explicit UNSPECIFIED occurrences.")
        return
    for item in items:
        context = item["rule_id"] or item["section"] or GRAMMAR_FILE
        print(f"{GRAMMAR_FILE}:{item['line']} [{context}] {item['text']}")


def print_show_result(result: dict[str, object]) -> None:
    if result["kind"] == "rule":
        print(result["text"])
        return
    print(f"{result['source']} :: {result['id']}")
    for record in result["records"]:
        print(json.dumps(record, ensure_ascii=False, sort_keys=False))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="repository root (default: current directory)")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    parser.add_argument("--summary", action="store_true", help="print mechanically derived repository summary and next IDs")
    parser.add_argument("--unresolved", action="store_true", help="list every explicit UNSPECIFIED occurrence with source context")
    parser.add_argument("--show", metavar="ID", help="show the exact canonical rule, lexeme, sense, or example for a stable ID")
    parser.add_argument("--json", action="store_true", help="emit discovery output as JSON; requires --summary, --unresolved, or --show")
    args = parser.parse_args(argv)

    discovery_requested = bool(args.summary or args.unresolved or args.show)
    if args.json and not discovery_requested:
        parser.error("--json requires --summary, --unresolved, or --show")

    root = Path(args.root).resolve()
    report = Report(errors=[], warnings=[])

    for rel in (GRAMMAR_FILE, LEXICON_FILE, EXAMPLES_FILE, SCHEMA_FILE):
        if not (root / rel).is_file():
            report.error(f"missing required file: {root / rel}")

    rules: set[str] = set()
    pos_codes: set[str] = set()
    custom_abbr: set[str] = set()
    lex_count = 0
    ex_count = 0

    if not report.errors:
        rules, pos_codes, custom_abbr = parse_grammar(root / GRAMMAR_FILE, report)
        lexeme_ids, _sense_ids, lex_count = validate_lexicon(root / LEXICON_FILE, pos_codes, report)
        ex_count = validate_examples(root / EXAMPLES_FILE, rules, lexeme_ids, custom_abbr, report)
        validate_schema(root / SCHEMA_FILE, report)

    payload: dict[str, object] = {
        "validation": {
            "errors": report.errors,
            "warnings": report.warnings,
            "counts": {
                "grammar_rules": len(rules),
                "lexical_senses": lex_count,
                "examples": ex_count,
            },
        }
    }

    if not report.errors and discovery_requested:
        if args.summary:
            payload["summary"] = collect_summary(root, rules, pos_codes, custom_abbr)
        if args.unresolved:
            payload["unresolved"] = unresolved_items(root / GRAMMAR_FILE)
        if args.show:
            result = show_record(root, args.show)
            if result is None:
                report.error(f"no canonical record found for {args.show!r}")
                payload["validation"]["errors"] = report.errors
            else:
                payload["show"] = result

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        for message in report.warnings:
            print(f"WARN: {message}")
        for message in report.errors:
            print(f"ERROR: {message}")

        print(
            f"Checked: {len(rules)} grammar rules, {lex_count} lexical senses, "
            f"{ex_count} examples; {len(report.errors)} error(s), {len(report.warnings)} warning(s)."
        )

        if not report.errors:
            if args.summary:
                print_summary(payload["summary"])
            if args.unresolved:
                print_unresolved(payload["unresolved"])
            if args.show:
                print_show_result(payload["show"])

    if report.errors or (args.strict and report.warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())