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

### G-PHON-002 — Consonant inventory

**Statement:** The consonant phoneme inventory is /p b t d k g h s ɕ v m n r j/.

**Conditions:** The oral stops form three voiced–voiceless pairs, /p b t d k g/. The fricatives are /h s ɕ v/; /s ɕ/ form the sibilant contrast and /v/ has no voiceless phonemic counterpart. The remaining consonants are /m n r j/.

### Allophony

### G-PHON-003 — Layered phonological alternation

**Statement:** Minitongue permits productive phonological alternations together with stronger or partly lexicalized alternations in selected older, frequent, or grammatical material.

**Conditions:** Productive alternations include conditioned intervocalic stop weakening and limited nasal place assimilation as specified below. Their exact conditioning environments remain **UNSPECIFIED** where not stated by a dedicated rule.

### G-PHON-009 — Conditioned intervocalic stop weakening

**Statement:** In licensed intervocalic environments, voiceless stops /p t k/ may voice to [b d g], and voiced stops /b d g/ may undergo further lenition.

**Conditions:** The prosodic and morphological environments that license each stage, whether both stages can apply in one derivation, and the phonetic outputs of voiced-stop lenition are **UNSPECIFIED**.

### G-PHON-010 — Limited nasal place assimilation

**Statement:** /m n/ may assimilate in place of articulation before a following consonant, but assimilation is limited rather than automatic in every preconsonantal environment.

**Conditions:** The consonants and morphological or prosodic domains that trigger assimilation, and the resulting phonetic outputs, are **UNSPECIFIED**.

### Phonotactics

### G-PHON-004 — Syllable template

**Statement:** Canonical syllables have the shape `(C)V(C)`. Consonant clusters are not permitted within a syllable.

**Conditions:** A nucleus may contain one vowel phoneme or one canonical diphthong. Onset distribution beyond the explicitly restricted consonants is **UNSPECIFIED**.

### G-PHON-006 — Diphthong inventory

**Statement:** The canonical diphthongs are /ai ei ui/.

**Conditions:** These diphthongs constitute single heavy syllable nuclei for stress. The lexical status of other vowel sequences and their sequence-specific repair outputs are **UNSPECIFIED**; illicit vowel sequences created by morphology are subject to G-PHON-011.

### G-PHON-007 — Position-sensitive coda inventory

**Statement:** Medial codas permit /p b t d k g m n r s/. Word-final codas permit /t k n r s/. No other consonants occur in coda position.

**Depends on:** G-PHON-004

### G-PHON-008 — Onset-only consonants

**Statement:** /h ɕ j/ occur only in onset position and are prohibited in codas. /j/ occurs only before a vowel.

**Conditions:** Because G-PHON-007 exhaustively defines coda inventories, /v/ is also excluded from codas. Further restrictions on word-initial versus word-medial onsets are **UNSPECIFIED**.

**Depends on:** G-PHON-004 G-PHON-007

### Prosody

### G-PHON-005 — Weight-sensitive stress

**Statement:** Closed syllables and syllables containing /ai ei ui/ are heavy. Stress falls on the penultimate syllable by default; a heavy final syllable attracts final stress.

**Conditions:** Morphological suffix classes may override the phonological default by being stress-attracting or stress-neutral. The membership and behavior of those suffix classes are **UNSPECIFIED** until the relevant morphology is established.

**Depends on:** G-PHON-006 G-PHON-007

## Morphophonology

### G-PHON-011 — Morpheme-boundary repair hierarchy

**Statement:** When suffixation creates an illicit consonant or vowel sequence, the default repair priority is assimilation > fusion/contraction > deletion. The highest-ranked available process that yields a phonotactically legal output applies.

**Conditions:** The segment combinations targeted by each process, the direction and features of assimilation, the outputs of fusion/contraction, and deletion targets are **UNSPECIFIED**. Epenthesis is not part of the default repair hierarchy.

**Depends on:** G-PHON-004 G-PHON-006 G-PHON-007

The exact morphological domains of G-PHON-009 and G-PHON-010, and the concrete suffix classes referenced by G-PHON-005, remain **UNSPECIFIED** pending the establishment of canonical morphemes.

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

### G-MORPH-006 — Nominal case inventory and core alignment

**Statement:** The nominal case inventory is ABS, ERG, GEN, DAT, LOC, CONT, POS, and INS/COM. ABS marks transitive P and inactive S; ERG marks transitive A and active S. GEN marks dependency relations including possession, affiliation, and part–whole relations. DAT marks an affected personal domain. LOC marks general spatial reference, CONT marks bounded containment or inclusion, POS marks contact/configuration/position, and INS/COM marks instrumental or associative/comitative relations.

**Conditions:** The semantic or lexical criteria assigning intransitive S arguments to the active versus inactive class remain **UNSPECIFIED**. Differential marking conditions and the segmental forms of case suffixes remain **UNSPECIFIED**.

**Depends on:** G-SYN-002 G-SYN-003

### G-MORPH-007 — Nominal inflection template

**Statement:** The nominal template is `NOUN-(NUMBER)-(GEN)-CASE`, with number optional.

**Conditions:** GEN may occur as the sole case marker or as an inner case before an eligible outer case under G-MORPH-008. The inventory and forms of number marking remain **UNSPECIFIED**.

### G-MORPH-008 — Restricted genitive case stacking

**Statement:** GEN is the only case that productively stacks. It may precede DAT, LOC, CONT, POS, or INS/COM, yielding an inner dependency relation plus an outer clausal or semantic relation.

**Conditions:** GEN does not stack with ABS or ERG, and DAT, LOC, CONT, POS, and INS/COM do not productively stack with one another.

**Depends on:** G-MORPH-006 G-MORPH-007

### Pronominal and deictic systems

Person, number, clusivity, deixis, and any pronominally restricted alignment or case patterns are **UNSPECIFIED**.

### Verbal morphology

### G-MORPH-009 — Verbal morphology template

**Statement:** The verbal template is `DIRECTIONAL-OBJ/PAT-ROOT-AUX/APP-SUBJ/AGT-TENSE-ASPECT`.

**Conditions:** The segmental forms and distribution of OBJ/PAT and SUBJ/AGT indexing and the auxiliary inventory are **UNSPECIFIED**. Applicative morphology occupies the AUX/APP slot as specified below.

### G-MORPH-010 — Directional prefixes

**Statement:** The directional prefixes are `i-` positive/convergent, `a-` negative/divergent, and zero for neutral directionality. Their basic contrast is path-like convergence versus stable relation versus divergence; conventionalized abstract relational extensions are permitted by G-MORPH-011.

**Conditions:** DAT, LOC, CONT, POS, and INS/COM productively participate in the three-way directional system. GEN participates only in the lexically and semantically restricted environments specified by G-MORPH-011. ABS and ERG do not themselves license directional relational readings.

### G-MORPH-011 — Directional and case composition

**Statement:** A case identifies a semantic relation and the directional specifies change along that relation: `i-` establishes, enters, approaches, or increases the relation; zero presents a stable or neutral relation; `a-` exits, departs from, dissolves, or decreases the relation.

**Conditions:** Productive interpretations are organized as follows.

| Case | `i-` convergent | zero neutral | `a-` divergent |
| --- | --- | --- | --- |
| DAT | acquisition, receipt, benefit, increased affected involvement | recipient, beneficiary, experiencer, stable affected relation | loss, deprivation, withdrawal, decreased affected involvement |
| LOC | approach or arrival at a general spatial reference | at/near a reference location | departure or movement away from a reference |
| CONT | entry or placement into bounded inclusion | containment/inclusion | exit or removal from bounded inclusion |
| POS | assuming or causing a contact/configurational position | maintaining contact/configuration/position | leaving or removing from contact/configuration/position |
| INS/COM | association, joining, attachment, taking up as a means | accompaniment, association, instrument/means | dissociation, separation, detachment, cessation of use |

CONT may extend conventionally from physical containment to bounded abstract domains such as membership or states. POS may extend from literal support/contact to attachment, posture, or other lexically licensed configurations. Whether DAT productively extends further to possession, allegiance, or transfer of control is **UNSPECIFIED**.

GEN is exceptional: with predicates whose lexical semantics permit change in a genitive dependency relation, `i-` may establish belonging/dependency, zero may maintain it, and `a-` may dissolve it. Ordinary adnominal GEN is not directionally reinterpreted. The lexical classes licensing directional GEN remain **UNSPECIFIED**.

**Depends on:** G-MORPH-006 G-MORPH-010

### G-MORPH-012 — Tense and aspect suffixes

**Statement:** Tense follows subject/agent indexing and precedes aspect. `-i` marks nonpast and `-a` marks past. Zero aspect marks imperfective and `-n` marks perfective.

**Conditions:** The semantic boundaries of past versus nonpast and perfective versus imperfective, including any interaction with lexical aspect, remain **UNSPECIFIED**.

### G-MORPH-013 — Two applicative classes

**Statement:** Minitongue has two productive applicative classes. An affected applicative promotes a DAT participant. A general oblique applicative promotes an INS/COM, LOC, CONT, or POS participant.

**Conditions:** The segmental forms of both applicatives are **UNSPECIFIED**. GEN is not a productive applicative input. Applicatives occupy the AUX/APP position in G-MORPH-009.

**Depends on:** G-MORPH-006 G-MORPH-009

### G-MORPH-014 — Applicative promotion and directional interaction

**Statement:** An applied participant becomes an ABS core object and is eligible for OBJ/PAT indexing. When an applicative and directional target the same underlying relation, the applicative changes argument status while the directional preserves the convergent, neutral, or divergent interpretation of that relation.

**Conditions:** The treatment, case, and indexing of any pre-existing basic object after applicativization, including possible double-object behavior, are **UNSPECIFIED**.

**Depends on:** G-MORPH-010 G-MORPH-011 G-MORPH-013 G-SYN-003 G-SYN-006

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

**Conditions:** Active S takes ERG and inactive S takes ABS under G-MORPH-006. The semantic or lexical criteria assigning intransitive predicates or arguments to the two S classes, and their verbal indexing realizations, remain **UNSPECIFIED**.

### G-SYN-003 — Case and verbal indexing jointly identify arguments

**Statement:** Core argument identification uses both nominal case marking and verbal argument indexing.

**Conditions:** The case inventory is specified by G-MORPH-006. Case and/or indexing may be differential according to grammatical or semantic properties, and selected pronouns or historically older constructions may preserve distinct patterns. The indexing inventory, conditioning hierarchy, and distribution of differential marking remain **UNSPECIFIED**.

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

**Conditions:** The two applicative classes are specified by G-MORPH-013–014. Ditransitive argument structure, the behavior of the pre-existing object under applicativization, and any additional valency-changing operations remain **UNSPECIFIED**.

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
| CONT | containment case | Project-specific case label for bounded inclusion/containment. |
| POS | positional case | Project-specific case label for contact/configuration/position. |

## Variation and diachrony

Diachrony is modeled selectively. Explicit historical developments may be added when they explain important structural asymmetries, irregularities, or lexicalized morphology; otherwise a plausible historical motivation may remain implicit. Historical analyses do not create synchronic exceptions unless those exceptions are separately canonized.

## Open questions

The following matters remain **UNSPECIFIED** after the phonology/phonotactics design pass:

- onset distribution beyond the explicit coda exclusions and /h ɕ j/ onset-only restriction;
- whether non-diphthong vowel sequences may occur lexically, and the sequence-specific outputs of vowel repair;
- the exact prosodic and morphological environments and phonetic outputs of intervocalic stop weakening;
- the exact triggering environments and outputs of nasal place assimilation;
- the segment-specific mappings used by assimilation, fusion/contraction, and deletion in morpheme-boundary repair;
- the identity and behavior of stress-attracting and stress-neutral suffix classes;
- the entire orthographic system;
- POS inventory and all lexical entries;
- case-suffix forms, number morphology, and complete paradigms;
- semantic conditioning of the active–stative split;
- OBJ/PAT and SUBJ/AGT indexing forms, inventories, and conditioning;
- auxiliary inventory and behavior;
- conditioning of differential case and indexing;
- the lexical classes licensing directional GEN and whether DAT extends productively to possession, allegiance, or transfer of control;
- the segmental forms of the two applicatives, the treatment of a pre-existing object after applicativization, ditransitive argument structure, and any additional valency-changing operations;
- predicate-class membership and copular distribution;
- discourse rules for constituent-order flexibility and argument omission;
- negation, interrogation, coordination, subordination, relative clauses, and other constructions outside phases 0–3.

Canonical regression examples are not yet added because the lexicon remains empty and the segmental forms of case suffixes, indexing markers, and applicatives remain **UNSPECIFIED**. The directional and TAM forms are established, but complete examples would still require inventing canonical lexical and inflectional material.
