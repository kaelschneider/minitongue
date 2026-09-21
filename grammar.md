# Minitongue Grammar

This file is the canonical prose specification of Minitongue. Record accepted rules here; keep proposals in discussion until accepted.

## Metadata

| Key | Value |
| --- | --- |
| language_name | Minitongue |
| language_tag | x-minitongue |
| metalanguage | en |
| project_version | 0.1.0 |
| status | draft |

## Conventions

- Canonical rule IDs: `G-DOMAIN-NNN`, with domains `PHON`, `ORTH`, `MORPH`, `SYN`, `SEM`, `PRAG`, `DISC`, `LEX`.
- Lexeme IDs: `L-NNNN`; sense IDs: `L-NNNN-SNN`; example IDs: `EX-NNNN`.
- Store canonical pronunciation/transcription in IPA. TSV/JSON IPA fields contain bare IPA without slash or bracket delimiters.
- Interlinear examples follow the Leipzig Glossing Rules.
- Standard Leipzig abbreviations are accepted without duplication below. Add only project-specific abbreviations to the dedicated table.

<!--
Rule template (copy into the appropriate section and replace placeholders):

### G-SYN-001 — Short descriptive title

**Statement:** One clear, testable generalization.

**Conditions:** Optional environment, scope, or restrictions.

**Exceptions:** Optional explicitly licensed exceptions.

**Depends on:** G-MORPH-001

**Examples:** EX-0001 EX-0002
-->

## Phonology

### Phoneme inventory

<!-- Define consonants/vowels with IPA symbols. Tables are recommended. -->

### Allophony

<!-- Add G-PHON-* rules for conditioned realizations. -->

### Phonotactics

<!-- Syllable structure, permitted clusters, distributional restrictions. -->

### Prosody

<!-- Stress, tone, intonation, weight, rhythm as applicable. -->

## Morphophonology

<!-- Alternations triggered at morpheme/word boundaries. Use G-PHON-* or G-MORPH-* consistently according to project analysis. -->

## Orthography

<!-- Grapheme inventory, grapheme↔phoneme relations, capitalization, punctuation, word division. Add G-ORTH-* rules. -->

## Morphology

### Morphological profile

<!-- Isolating/agglutinative/fusional/polysynthetic tendencies; head/dependent marking; synthesis/fusion observations. -->

### Parts of speech

Declare every `lexicon.tsv` POS code here. Keep codes short, stable, and machine-friendly.

| Code | Name | Notes |
| --- | --- | --- |

### Nominal morphology

<!-- Number, case, definiteness, possession, classifiers, agreement, etc. -->

### Pronominal and deictic systems

<!-- Person, number, clusivity, gender/noun class, deixis, politeness if applicable. -->

### Verbal morphology

<!-- TAM, mood, polarity, voice/valency, agreement/indexing, non-finite forms. -->

### Derivation and compounding

<!-- Productive derivation, conversion, compounding, lexicalization constraints. -->

### Paradigms

<!-- Keep productive paradigm rules and compact illustrative tables here. Representative/edge forms belong in examples.tsv. -->

## Syntax

### Constituent order

<!-- Clause-level and phrase-level ordering; information-structure-conditioned variants. -->

### Noun phrase

<!-- Determiners, modifiers, possession, numerals, relative clauses, agreement. -->

### Clause structure

<!-- Argument structure, alignment, grammatical relations, copular/existential clauses. -->

### Negation

<!-- Standard and nonstandard negation; scope interactions. -->

### Interrogatives

<!-- Polar/content questions, interrogative placement/particles/intonation. -->

### Coordination and subordination

<!-- Coordination, complement clauses, adverbial clauses, clause chaining. -->

### Relative clauses

<!-- Strategy, accessibility, head position, resumptives/gaps, relativizers. -->

## Semantics

<!-- Lexical/grammatical semantic distinctions that constrain interpretation. Add G-SEM-* rules. -->

## Pragmatics and discourse

<!-- Information structure, deixis, politeness, discourse particles, ellipsis, reference tracking. Add G-PRAG-* / G-DISC-* rules. -->

## Lexical conventions

<!-- Lexical-class conventions or productive lexical rules not better captured elsewhere. Add G-LEX-* rules. -->

## Glossing conventions

Examples must follow the Leipzig Glossing Rules. Standard Leipzig abbreviations are built into `scripts/validate.py` and need not be repeated here.

### Project-specific gloss abbreviations

Add only abbreviations not covered by the Leipzig standard list.

| Abbreviation | Meaning | Notes |
| --- | --- | --- |

## Variation and diachrony

<!-- Optional: registers, dialects, historical stages, sound changes. State clearly whether forms are canonical or variant. -->

## Open questions

<!-- Noncanonical design questions may be tracked here only if clearly marked as unresolved and never cited as rules. -->