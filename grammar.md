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

**Conditions:** Productive alternations include consonant gradation under G-PHON-009 and limited nasal place assimilation as specified below. Conditioning remains **UNSPECIFIED** only where not stated by a dedicated rule.

### G-PHON-009 — Productive strong–weak consonant gradation

**Statement:** In gradating morphology, the strong grades /p t k/ alternate respectively with the weak grades /v d g/.

**Conditions:** Grade is selected morphophonologically by the relevant construction or suffix class. A specified morphological grade overrides what modern surface stress or syllable weight alone would predict. Inflection is the principal productive domain; derivation normally does not trigger gradation unless an older derivational construction is explicitly specified. Older suffixes may preserve lexical grade selection, while newly established productive morphology may align grade selection with the historical stress-conditioned pattern described by G-PHON-018. The concrete suffixes and constructions selecting STRONG or WEAK grade remain **UNSPECIFIED** until their morphemes are established.

**Depends on:** G-PHON-005

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

### G-PHON-016 — Inherited extra-weak consonant grade

**Statement:** Selected inherited morphology may preserve a third, extra-weak grade with the correspondences /p ~ v ~ ∅/, /t ~ d ~ r/, and /k ~ g ~ j/.

**Conditions:** The extra-weak grade is not productively assigned to new lexemes or constructions. Its surviving forms must be established as inherited members of particular paradigms or morphological constructions. Zero grade is restricted to inherited forms in which historical /v/ deletion produced a phonotactically licensed vowel sequence. Extra-weak /j/ derived from /g/ is written ⟨ğ⟩ under G-ORTH-003.

**Depends on:** G-PHON-009

### G-PHON-017 — Rhotic realization

**Statement:** The phoneme /r/, including /r/ that continues the inherited extra-weak coronal grade, is realized as [ɾ] intervocalically and [r] elsewhere.

**Conditions:** [ɾ] is an allophone of /r/, not a separate phoneme.

The exact triggering environments of G-PHON-010, the concrete suffixes selecting STRONG or WEAK under G-PHON-009, the inventory of inherited constructions preserving G-PHON-016, and the concrete suffix classes referenced by G-PHON-005 remain **UNSPECIFIED** pending the establishment of canonical morphemes and lexemes.

## Orthography

### G-ORTH-001 — Palatal glide spelling

**Statement:** The phoneme /j/ is normally written ⟨y⟩.

**Exceptions:** /j/ that is the inherited extra-weak grade of /g/ is written ⟨ğ⟩ under G-ORTH-003.

### G-ORTH-002 — Alveolo-palatal fricative spelling

**Statement:** The phoneme /ɕ/ is written ⟨c⟩. Consequently, /ɕi/ is written ⟨ci⟩.

**Conditions:** All other grapheme-to-phoneme correspondences beyond G-ORTH-001–003, capitalization, punctuation, and word-division rules are **UNSPECIFIED**.

### G-ORTH-003 — Historical velar glide spelling

**Statement:** /j/ that continues the inherited extra-weak grade of /g/ is written ⟨ğ⟩, yielding the morphophonemic orthographic correspondence ⟨k⟩ ~ ⟨g⟩ ~ ⟨ğ⟩.

**Conditions:** ⟨ğ⟩ does not represent a phoneme distinct from /j/; ordinary /j/ remains ⟨y⟩ under G-ORTH-001.

**Depends on:** G-PHON-016 G-ORTH-001

## Morphology

### Morphological profile

### G-MORPH-001 — High but layered synthesis

**Statement:** Minitongue permits high morphological synthesis, but substantial grammatical packaging is concentrated in selected domains rather than required uniformly across all word classes and constructions.

### G-MORPH-002 — Affixation-centered morphology and compounding

**Statement:** Affixation is the primary productive morphological mechanism. Compounding is also a major productive strategy for lexical word formation.

**Conditions:** The use of clitics and reduplication is **UNSPECIFIED**. Productive stem alternation includes the strong–weak consonant gradation specified by G-PHON-009.

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

The following sound changes are **experimental historical laws** on the `experimental` branch. They describe a proposed diachronic derivation and do not by themselves establish productive synchronic alternations.

### G-PHON-012 — Pre-/i/ palatalization and merger

**Statement:** Proto sequences *ki and *ti merge before /i/ through a palatalized/affricated stage and surface as modern /ɕi/, written ⟨ci⟩.

**Historical path:** *ki, *ti > *tɕi > /ɕi/.

**Ordering:** This change precedes G-PHON-013 and G-PHON-014, so /t/ created later from word-final *p does not feed this palatalization.

**Depends on:** G-ORTH-002

### G-PHON-013 — Word-final *p coronalization

**Statement:** Proto *p becomes *t at the end of a phonological word.

**Historical law:** *p > *t / _#.

### G-PHON-014 — Word-final *t assibilation

**Statement:** Word-final *t, including *t derived by G-PHON-013, becomes /s/.

**Historical law:** *t > *s / _#.

**Depends on:** G-PHON-013

### G-PHON-015 — Word-initial *p lenition and debuccalization

**Statement:** Proto *p at the beginning of a phonological word lenites through *ɸ and becomes /h/.

**Historical path:** *p > *ɸ > /h/ / #_.

**Conditions:** Proto *p not targeted by a word-edge law remains /p/, including *p that is word-medial because of surrounding morphological material. The ordering of G-PHON-015 relative to G-PHON-012–014 is not contrastive in the currently specified environments. Whether any resulting /h ~ p ~ s/ or /k ~ ɕ/, /t ~ ɕ/ alternations are synchronically productive is **UNSPECIFIED**.

### G-PHON-018 — Historical stress-conditioned strong–weak gradation

**Statement:** In eligible stem-internal intervocalic position, proto *p, *t, and *k retained their strong stop grade before a stressed vowel and developed the weak grades /v d g/ before an unstressed vowel.

**Historical paths:** *p > *b > *β > /v/; *t > /d/; *k > /g/ in the weak environment. Strong *p, *t, and *k were retained.

**Conditions:** This stress-conditioned distribution is the historical source of modern G-PHON-009. Subsequent morphological reanalysis made construction- or suffix-selected grade primary synchronically. The word-edge *p changes in G-PHON-013–015 occupy separate environments.

**Ordering:** G-PHON-012 precedes this gradation, so proto *ki and *ti undergo the older pre-/i/ merger before surviving velars and coronals participate in gradation.

**Depends on:** G-PHON-012

### G-PHON-019 — Historical extra-weak labial deletion

**Statement:** In selected older morphology, weak-grade /v/ in an unstressed intervocalic environment could delete, producing the extra-weak labial grade ∅.

**Conditions:** Deletion applied only where the resulting vowel sequence was licensed by the phonotactics of the relevant historical stage; otherwise /v/ was retained. The modern zero grade is inherited and nonproductive under G-PHON-016.

**Depends on:** G-PHON-016 G-PHON-018

### G-PHON-020 — Historical extra-weak coronal rhotacism

**Statement:** In selected older morphology, weak-grade /d/ underwent further intervocalic lenition through *[ð̞] and *[ɾ], after which the tap merged phonemically with /r/.

**Historical path:** *d > *[ð̞] > *[ɾ] > /r/.

**Conditions:** The resulting /r/ participates in the general modern allophony of G-PHON-017. The extra-weak coronal grade is inherited and nonproductive under G-PHON-016.

**Depends on:** G-PHON-016 G-PHON-017 G-PHON-018

### G-PHON-021 — Historical extra-weak velar gliding

**Statement:** In selected older morphology, weak-grade /g/ underwent further palatal lenition before /i e/, ultimately yielding /j/.

**Historical path:** *g > *[ɣʲ] > *[j] / _{i,e}.

**Conditions:** The original front-vowel conditioning was later morphologized. In inherited modern paradigms the extra-weak /j/ may therefore occur before any vowel and is written ⟨ğ⟩ under G-ORTH-003. This grade is nonproductive under G-PHON-016.

**Ordering:** G-PHON-012 precedes G-PHON-018 and this change; ordinary proto *ki therefore undergoes the earlier *ki/*ti > /ɕi/ merger rather than first becoming *gi or /j/. Any lexical exception must be separately established.

**Depends on:** G-PHON-012 G-PHON-016 G-PHON-018 G-ORTH-003

## Open questions

The following matters remain **UNSPECIFIED** after the phonology/phonotactics design pass:

- onset distribution beyond the explicit coda exclusions and /h ɕ j/ onset-only restriction;
- whether non-diphthong vowel sequences may occur lexically, and the sequence-specific outputs of vowel repair;
- the exact triggering environments and outputs of nasal place assimilation;
- the segment-specific mappings used by assimilation, fusion/contraction, and deletion in morpheme-boundary repair;
- the identity and behavior of stress-attracting and stress-neutral suffix classes;
- all orthographic correspondences except ordinary /j/ ⟨y⟩, inherited extra-weak /j/ < *g ⟨ğ⟩, and /ɕ/ ⟨c⟩, plus capitalization, punctuation, and word division;
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
