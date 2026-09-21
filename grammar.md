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

## Design brief

Minitongue is designed as a deliberate hybrid: naturalistic plausibility, compactness, and a distinctive structural identity are balanced rather than maximized independently. The language permits moderately naturalistic complexity, including redundancy, asymmetry, and limited irregularity, while retaining economy as a design constraint.

Historical development is modeled selectively. Important subsystems may receive explicit lightweight diachronic analyses, while other synchronic patterns may have only an implied plausible history. Productive structure should remain learnable and economical; distinctive or information-dense structure may be concentrated in selected domains rather than distributed uniformly throughout the language.

## Conventions

- Canonical rule IDs: `G-DOMAIN-NNN`, with domains `PHON`, `ORTH`, `MORPH`, `SYN`, `SEM`, `PRAG`, `DISC`, `LEX`.
- Lexeme IDs: `L-NNNN`; sense IDs: `L-NNNN-SNN`; example IDs: `EX-NNNN`.
- Store canonical pronunciation/transcription in IPA. TSV/JSON IPA fields contain bare IPA without slash or bracket delimiters.
- Interlinear examples follow the Leipzig Glossing Rules.
- Standard Leipzig abbreviations are accepted without duplication below. Add only project-specific abbreviations to the dedicated table.

## Phonology

### Phoneme inventory

### G-PHON-001 — Vowel inventory

**Statement:** The vowel phoneme inventory is /i e a u/.

### G-PHON-002 — Consonant inventory architecture

**Statement:** The consonant system contains approximately 10–14 phonemes and uses a voiced-versus-voiceless distinction as a principal contrast among obstruents.

**Conditions:** The exact consonant phonemes, the extent of the voicing series, and any additional place or manner contrasts are **UNSPECIFIED**.

### Allophony

### G-PHON-003 — Layered phonological alternation

**Statement:** Minitongue permits productive phonological alternations together with stronger or partly lexicalized alternations in selected older, frequent, or grammatical material.

**Conditions:** The actual alternations, their environments, and their lexical domains are **UNSPECIFIED**.

### Phonotactics

### G-PHON-004 — Syllable template

**Statement:** Canonical syllables have the shape `(C)V(C)`. Consonant clusters are not permitted within a syllable.

**Conditions:** The permitted onset and coda consonants and cross-morpheme repair strategies are **UNSPECIFIED**.

### Prosody

### G-PHON-005 — Weight-sensitive stress

**Statement:** Stress assignment is sensitive to syllable weight and uses a regular fallback when no syllable satisfies the relevant weight condition.

**Conditions:** The definition of syllable weight, direction of stress computation, and fallback position are **UNSPECIFIED**.

## Morphophonology

The interaction between suffixation and the no-cluster phonotactic constraint is **UNSPECIFIED**. In particular, Minitongue has not yet established whether potentially illicit cross-morpheme consonant sequences are avoided lexically or repaired by epenthesis, deletion, assimilation, allomorphy, or another process.

## Orthography

The grapheme inventory, grapheme-to-phoneme correspondences, capitalization, punctuation, and word-division rules are **UNSPECIFIED**.

## Morphology

### Morphological profile

### G-MORPH-001 — High but layered synthesis

**Statement:** Minitongue permits high morphological synthesis, but substantial grammatical packaging is concentrated in selected domains rather than required uniformly across all word classes and constructions.

### G-MORPH-002 — Affixation-centered morphology and compounding

**Statement:** Affixation is the primary productive morphological mechanism. Compounding is also a major productive strategy for lexical word formation.

**Conditions:** The use of clitics, reduplication, and productive stem alternation is **UNSPECIFIED**.

### G-MORPH-003 — Predominantly suffixing directionality

**Statement:** Productive affixation is predominantly suffixing: grammatical and derivational material normally follows the root or stem.

**Exceptions:** Historically older or highly grammaticalized material may occur outside the dominant suffixing pattern when such forms are explicitly established.

### G-MORPH-004 — Layered fusion and exponence

**Statement:** Productive morphology is predominantly agglutinative and segmentable, but limited fusion is permitted. Older or high-frequency morphology may exhibit cumulative exponence, irregular allomorphy, or less transparent morpheme boundaries, and different morphological domains may differ in degree of fusion.

### Parts of speech

Declare every `lexicon.tsv` POS code here. Keep codes short, stable, and machine-friendly.

| Code | Name | Notes |
| --- | --- | --- |

### Nominal morphology

The case inventory, nominal inflectional categories, and differential case-marking conditions are **UNSPECIFIED**.

### Pronominal and deictic systems

Person, number, clusivity, deixis, and any pronominally restricted alignment or case patterns are **UNSPECIFIED**.

### Verbal morphology

The inventory and ordering of verbal categories, argument-indexing exponence, TAM categories, and valency-changing affixes are **UNSPECIFIED**.

### Derivation and compounding

### G-MORPH-005 — Productive layered derivation

**Statement:** Derivational morphology is highly productive and may stack compositionally. Productivity may vary by semantic or lexical domain, and older derived formations may become semantically opaque or morphophonologically irregular.

**Depends on:** G-MORPH-002 G-MORPH-003 G-MORPH-004

### Paradigms

No complete inflectional or derivational paradigms are specified yet.

## Syntax

### Constituent order

### G-SYN-001 — Default SOV/APV order with licensed flexibility

**Statement:** The neutral basic order is SOV for intransitive clauses and A-P-V for transitive clauses. Alternative constituent orders are permitted when grammatical marking keeps argument roles recoverable.

**Conditions:** The discourse and information-structural conditions licensing alternative orders are **UNSPECIFIED**.

### Noun phrase

Internal noun-phrase order and agreement are **UNSPECIFIED**.

### Clause structure

### G-SYN-002 — Active–stative / ergative–absolutive alignment

**Statement:** Core alignment combines ergative–absolutive organization with an active–stative split. Transitive A and P are grammatically distinguished. Intransitive S arguments divide into an A-like class and a P-like class rather than forming a single uniform S category.

**Conditions:** The semantic or lexical criteria assigning intransitive predicates or arguments to the two S classes, and the exact case or indexing realizations of those classes, are **UNSPECIFIED**.

### G-SYN-003 — Case and verbal indexing jointly identify arguments

**Statement:** Core argument identification uses both nominal case marking and verbal argument indexing.

**Conditions:** Case and/or indexing may be differential according to grammatical or semantic properties, and selected pronouns or historically older constructions may preserve distinct patterns. The case inventory, indexing inventory, conditioning hierarchy, and distribution of differential marking are **UNSPECIFIED**.

**Depends on:** G-SYN-002

### G-SYN-004 — Predicate-centered split predicate system

**Statement:** Verbs, adjectives, and some nouns may function directly as predicates and may share portions of the inflectional system. Predicate classes need not behave identically, and some nonverbal predicates may require copular or auxiliary support.

**Exceptions:** Older copular or auxiliary constructions may survive in restricted environments once explicitly established.

**Conditions:** The predicate classes, shared inflectional categories, and distribution of copular material are **UNSPECIFIED**.

### G-SYN-005 — Argument omission and valency are distinct

**Statement:** Core arguments that are recoverable from verbal indexing and discourse context may be omitted frequently. Omission is differentially constrained by argument type and/or discourse status. True changes in predicate valency are handled by productive morphological operations rather than by argument omission alone.

**Conditions:** The exact omission constraints, discourse licensing conditions, and valency-changing operations are **UNSPECIFIED**.

**Depends on:** G-SYN-003 G-MORPH-001 G-MORPH-003

### G-SYN-006 — Core valency coverage

**Statement:** The grammar distinguishes intransitive, transitive, and ditransitive predicate frames and permits productive morphological operations that change valency.

**Conditions:** The argument structure of ditransitives, the inventory of valency operations, and their morphological forms are **UNSPECIFIED**.

**Depends on:** G-SYN-005

### Negation

**UNSPECIFIED**.

### Interrogatives

**UNSPECIFIED**.

### Coordination and subordination

**UNSPECIFIED**.

### Relative clauses

**UNSPECIFIED**.

## Semantics

The semantic conditioning of the active–stative split, differential marking, and derivational productivity is **UNSPECIFIED** beyond the structural requirements stated above.

## Pragmatics and discourse

Information-structure rules governing constituent-order flexibility and argument omission are **UNSPECIFIED**.

## Lexical conventions

No canonical lexical classes or lexical entries have yet been established beyond the structural categories described above.

## Glossing conventions

Examples must follow the Leipzig Glossing Rules. Standard Leipzig abbreviations are built into `scripts/validate.py` and need not be repeated here.

### Project-specific gloss abbreviations

Add only abbreviations not covered by the Leipzig standard list.

| Abbreviation | Meaning | Notes |
| --- | --- | --- |

## Variation and diachrony

Diachrony is modeled selectively. Explicit historical developments may be added when they explain important structural asymmetries, irregularities, or lexicalized morphology; otherwise a plausible historical motivation may remain implicit. Historical analyses do not create synchronic exceptions unless those exceptions are separately canonized.

## Open questions

The following matters remain **UNSPECIFIED** after design phases 0–3:

- exact consonant inventory and distribution;
- onset/coda restrictions and all phonotactic sequencing constraints beyond `(C)V(C)`;
- syllable-weight definition, stress direction, and fallback stress;
- concrete allophonic and morphophonological processes;
- repair of consonant sequences created by suffixation;
- the entire orthographic system;
- POS inventory and all lexical entries;
- actual affix forms, morpheme-order templates, and paradigms;
- case inventory and the formal realization of active–stative / ergative–absolutive alignment;
- semantic conditioning of the active–stative split;
- verbal indexing categories and their ordering/exponence;
- conditioning of differential case and indexing;
- predicate-class membership and copular distribution;
- valency-changing morphemes and ditransitive argument structure;
- discourse rules for constituent-order flexibility and argument omission;
- negation, interrogation, coordination, subordination, relative clauses, and other constructions outside phases 0–3.

Canonical regression examples are not yet added because orthography, lexical forms, and the relevant grammatical morphemes remain **UNSPECIFIED**. Creating full examples now would require inventing canonical forms that the design survey did not establish.
