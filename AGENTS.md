# AGENTS.md

## Purpose

This repository is the canonical, human-readable specification of Minitongue. Keep it small, deterministic, and easy for humans and language models to inspect.

## Repository governance

Use only these branches:

- `main` — canonical, accepted language state.
- `experimental` — provisional or exploratory work that is not yet canonical.

Do not create, rename, delete, or use additional branches unless the user explicitly requests it.

Do not alter the repository structure unless the user explicitly requests a structural change. This includes adding, deleting, renaming, moving, or reorganizing files or directories. New linguistic content must fit the established files by default.

When branch choice matters, accepted canonical changes belong on `main`; exploratory changes belong on `experimental`.

## Read order

Before changing language data:

1. Read this file.
2. Read only the relevant section(s) of `grammar.md`.
3. Read only the relevant rows/columns of `lexicon.tsv` and `examples.tsv`.
4. Read `schema.json` only for data-shape, interchange, or TEI work.
5. Run `python scripts/validate.py` after edits.

Do not treat chat history as canonical language data.

## Repository map

```text
minitongue/
├── AGENTS.md          # workflow and file contracts
├── grammar.md         # canonical linguistic rules + controlled vocabularies
├── lexicon.tsv        # canonical lexemes; one row per sense
├── examples.tsv       # canonical examples + regression cases
├── schema.json        # normalized JSON shape + TEI mapping hints
└── scripts/
    └── validate.py    # deterministic repository checks
```

`grammar.md`, `lexicon.tsv`, and `examples.tsv` own linguistic facts. `schema.json` describes derived interchange data and must not introduce new linguistic facts.

## Canonicality

- The human creator has final authority.
- Suggestions are proposals until explicitly accepted and written to canonical files.
- If a fact is missing, use `UNSPECIFIED`; do not infer a rule just to complete an analysis.
- Preserve stable IDs. Never recycle or renumber IDs for cosmetic reasons.
- Prefer minimal diffs. Do not reformat unrelated rows or sections.
- Do not add files or dependencies unless requested or clearly necessary.

## `grammar.md`

Owns phonology, morphophonology, orthography, morphology, syntax, semantics/pragmatics, discourse conventions, POS codes, and project-specific gloss abbreviations.

Canonical rule headings use:

```text
### G-DOMAIN-NNN — Short rule title
```

Allowed domains: `PHON`, `ORTH`, `MORPH`, `SYN`, `SEM`, `PRAG`, `DISC`, `LEX`.

Each rule should state one testable generalization and may cite dependencies and example IDs. Keep productive paradigms here as rules or compact Markdown tables; use `examples.tsv` for representative and edge-case forms. Do not add `paradigms.tsv` unless machine-addressable paradigms become necessary at scale.

## `lexicon.tsv`

UTF-8 TSV, one row per sense. The exact header is enforced by `validate.py`.

- `lexeme_id`: stable `L-0001` style ID.
- `lemma`: canonical orthographic citation form.
- `ipa`: bare Unicode IPA.
- `pos`: code declared in `grammar.md`.
- `features`: one-line JSON object; lexeme-level.
- `etymology`: lexeme-level text.
- `sense_id`: stable `L-0001-S01` style ID.
- `definition`, `usage`, `notes`: sense-level text.

Rows sharing a `lexeme_id` must agree on `lemma`, `ipa`, `pos`, `features`, and `etymology`.

## `examples.tsv`

UTF-8 TSV and the regression corpus. The exact header is enforced by `validate.py`.

Use stable `EX-0001` IDs and judgments `grammatical`, `ungrammatical`, or `marginal`. Every row contains orthographic text, bare IPA, segmentation, Leipzig gloss, idiomatic translation, and `rule_refs`. `violated_rule_refs` is required for ungrammatical examples. `lexeme_refs` is optional.

Prefer paired positive/negative regression examples for constraints when useful.

## IPA and Leipzig

IPA is mandatory for canonical pronunciation/transcription. Store bare IPA in TSV/JSON; add `/.../` or `[...]` only in presentation. `validate.py` checks presence, NFC normalization, and delimiter hygiene, but phonological correctness remains governed by `grammar.md`.

Follow the Leipzig Glossing Rules:

- align `segmentation` and `gloss` word-by-word;
- mirror `-` morpheme boundaries and `=` clitic boundaries;
- use periods for one-to-many correspondences;
- use conventional uppercase grammatical labels;
- use standard Leipzig abbreviations when applicable;
- declare only project-specific/nonstandard abbreviations in `grammar.md`.

The validator also checks matching `~` reduplication and angle-bracket infix markers when present. It does not infer morphological analysis.

## Data conventions

- UTF-8 without BOM; Unicode NFC.
- IDs are immutable once published.
- Reference lists are whitespace-separated IDs, without commas.
- JSON inside TSV cells is a one-line object; use `{}` when empty.
- Avoid embedded tabs/newlines so Git diffs remain one logical record per line.
- Keep lexical glosses lower-case where practical; reserve uppercase gloss tokens for grammatical categories.

## TEI mapping

`schema.json` uses JSON Schema Draft 2020-12 plus nonstandard `x-tei` mapping hints. Intended mappings include `entry` for lexemes, `form/orth` for lemmas, `pron notation="IPA"` for IPA, `gramGrp/pos` for POS, `sense/def` for senses, `cit type="example"` with nested translation citations for examples, and `fs`/`f` for structured linguistic features.

These are project mappings, not TEI conformance. Validate generated XML independently against the chosen TEI P5 ODD/schema.

## Change workflow

1. Identify governing rule/lexeme/sense/example IDs.
2. Decide whether the request is already licensed, underspecified, or contradictory.
3. Make the smallest coherent accepted change.
4. Update dependent references and regression examples.
5. Run `python scripts/validate.py` from the repository root.
6. Resolve every error before considering the change complete.

If changing file structure or column names, update `AGENTS.md`, `schema.json`, and `scripts/validate.py` together.

## Representation-bootstrap lexicon selection

Build the initial lexicon as a small diagnostic set rather than as broad basic vocabulary. Prefer lexemes that test several dimensions at once: semantic class, lexical valency, root shape, grade behavior, phonological or morphophonological behavior, case selection, applicative compatibility, and explanatory diachrony. Include ordinary control items as well as forms expected to trigger important alternations.

## Representation-bootstrap acceptance test

The representation bootstrap is not complete merely when citation forms or isolated paradigms exist. Its minimum canonical regression coverage should demonstrate:

- active intransitive S;
- inactive intransitive S;
- ordinary transitive A–P;
- zero ABS versus an overt non-ABS case;
- nominal number;
- a stative/property predicate;
- a verbal grade contrast;
- both OBJ/PAT and SUBJ/AGT indexing domains;
- directional morphology;
- the affected applicative;
- the general oblique applicative;
- at least one significant morphophonological repair; and
- a short connected passage using only established canonical material.

If that connected passage requires an unanticipated construction, mark the construction `UNSPECIFIED` and design it explicitly rather than patching the text.

## Definition of done

Canonical files agree; IDs and references resolve; IPA/Leipzig mechanical checks pass; JSON-in-TSV parses; and `python scripts/validate.py` exits 0.