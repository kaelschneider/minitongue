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

### G-PHON-010 — Nasal place assimilation

**Statement:** /n/ assimilates in place to an immediately following place-bearing consonant, both within a morpheme and across a morpheme boundary.

**Outputs:** Before labial consonants, /n/ surfaces as [m]; before coronal consonants, it surfaces as [n]; before dorsal or palatal consonants, it surfaces as [ŋ]. These are conditioned surface realizations of /n/ and do not add /ŋ/ to the phoneme inventory.

**Conditions:** The output before placeless /h/ is **UNSPECIFIED**. Underlying /m/ is not subject to this rule.

### Phonotactics

### G-PHON-004 — Syllable template

**Statement:** Canonical syllables have the shape `(C)V(C)`. Consonant clusters are not permitted within a syllable.

**Conditions:** A nucleus may contain one vowel phoneme or one canonical diphthong. Every consonant phoneme is licensed in onset position; there are no additional general restrictions distinguishing word-initial from word-medial onsets.

### G-PHON-006 — Diphthong inventory and lexical vowel sequences

**Statement:** The canonical diphthongs are /ai ei ui/. Other vowel sequences are prohibited within lexical roots.

**Conditions:** The canonical diphthongs constitute single heavy syllable nuclei for stress. When morphology creates a non-diphthong vowel sequence, the sequence is repaired by contraction/fusion under G-PHON-011. Contraction is sequence-specific: no single vowel-dominance rule applies. The explicit output mapping for each ordered pair of /i e a u/ remains **UNSPECIFIED**.

### G-PHON-007 — Position-sensitive coda inventory

**Statement:** Medial codas permit /p b t d k g m n r s/. Word-final codas permit /t k n r s/. No other consonants occur in coda position.

**Depends on:** G-PHON-004

### G-PHON-008 — Onset-only consonants

**Statement:** /h ɕ j/ occur only in onset position and are prohibited in codas. /j/ occurs only before a vowel.

**Conditions:** Because G-PHON-007 exhaustively defines coda inventories, /v/ is also excluded from codas. All consonant phonemes are otherwise licensed as onsets both word-initially and word-medially.

**Depends on:** G-PHON-004 G-PHON-007

### Prosody

### G-PHON-005 — Weight-sensitive stress and suffix stress classes

**Statement:** Closed syllables and syllables containing /ai ei ui/ are heavy. Stress falls on the penultimate syllable by default; a heavy final syllable attracts final stress.

**Suffix classes:** Suffixes belong to one of three prosodic classes when established: (1) stress-neutral suffixes do not alter the stem's stress domain; (2) self-stressing suffixes bear stress themselves; and (3) pre-stressing suffixes assign stress to the immediately preceding stem syllable.

**Gradation interaction:** The three-way stress classification is compatible with the historical source of G-PHON-009: self-stressing suffixes naturally align with WEAK grade and pre-stressing suffixes with STRONG grade in newly established productive morphology. Synchronically, however, grade is selected morphologically under G-PHON-009 rather than recalculated from surface stress. Stress-neutral suffixes do not by themselves determine grade. The actual suffix membership of each stress class and each suffix's grade selection remain **UNSPECIFIED** until the morphemes are established.

**Depends on:** G-PHON-006 G-PHON-007 G-PHON-009

## Morphophonology

### G-PHON-011 — Morpheme-boundary repair hierarchy

**Statement:** When suffixation creates an illicit consonant or vowel sequence, repair applies in the ordered hierarchy assimilation > fusion/contraction > deletion. The highest-ranked available process that yields a phonotactically legal output applies. Epenthesis is not part of the default hierarchy.

**Conditions:** Nasal assimilation uses the mappings in G-PHON-010. Illicit non-diphthong vowel sequences use sequence-specific contraction/fusion rather than a general deletion or vowel-dominance rule. The explicit contraction table for ordered vowel pairs, the non-nasal consonant pairs that undergo assimilation or fusion, their outputs, and the deletion target for otherwise unrepaired sequences remain **UNSPECIFIED**.

**Depends on:** G-PHON-004 G-PHON-006 G-PHON-007 G-PHON-010

### G-PHON-016 — Inherited extra-weak consonant grade

**Statement:** Selected inherited morphology may preserve a third, extra-weak grade with the correspondences /p ~ v ~ ∅/, /t ~ d ~ r/, and /k ~ g ~ j/.

**Conditions:** The extra-weak grade is not productively assigned to new lexemes or constructions. Its surviving forms must be established as inherited members of particular paradigms or morphological constructions. Zero grade is restricted to inherited forms in which historical /v/ deletion produced a phonotactically licensed vowel sequence. Extra-weak /j/ derived from /g/ is written ⟨ğ⟩ under G-ORTH-003.

**Depends on:** G-PHON-009

### G-PHON-017 — Rhotic realization

**Statement:** The phoneme /r/, including /r/ that continues the inherited extra-weak coronal grade, is realized as [ɾ] intervocalically and [r] elsewhere.

**Conditions:** [ɾ] is an allophone of /r/, not a separate phoneme.

The output of G-PHON-010 before /h/, the concrete suffixes selecting STRONG or WEAK under G-PHON-009, the inventory of inherited constructions preserving G-PHON-016, the membership of the three stress classes in G-PHON-005, and the remaining segment-specific repair mappings in G-PHON-011 remain **UNSPECIFIED** pending the establishment of canonical morphemes and lexemes.

## Orthography

### G-ORTH-001 — Palatal glide spelling

**Statement:** The phoneme /j/ is normally written ⟨y⟩.

**Exceptions:** /j/ that is the inherited extra-weak grade of /g/ is written ⟨ğ⟩ under G-ORTH-003.

### G-ORTH-002 — Alveolo-palatal spelling

**Statement:** The phoneme /ɕ/ is written ⟨c⟩. Consequently, /ɕi/ is written ⟨ci⟩.

**Inherited inflectional exception:** In the semantic-primal conjugation, historical 2.NONPAST *-ti is also written ⟨ci⟩. It is pronounced [tɕi] when it heads an open syllable and [ɕi] when the syllable is closed under G-PHON-012. This is an inherited morphophonemic spelling and does not add /tɕ/ to the phoneme inventory.

### G-ORTH-003 — Historical velar glide spelling

**Statement:** /j/ that continues the inherited extra-weak grade of /g/ is written ⟨ğ⟩, yielding the morphophonemic orthographic correspondence ⟨k⟩ ~ ⟨g⟩ ~ ⟨ğ⟩.

**Conditions:** ⟨ğ⟩ does not represent a phoneme distinct from /j/; ordinary /j/ remains ⟨y⟩ under G-ORTH-001.

**Depends on:** G-PHON-016 G-ORTH-001

### G-ORTH-004 — Transparent phonemic spelling

**Statement:** Outside the explicitly historical ⟨ğ⟩ spelling in G-ORTH-003, the orthography is maximally transparent and uses one grapheme per phoneme wherever the established Latin inventory permits.

| Phoneme | Grapheme |
| --- | --- |
| /i/ | ⟨i⟩ |
| /e/ | ⟨e⟩ |
| /a/ | ⟨a⟩ |
| /u/ | ⟨u⟩ |
| /p/ | ⟨p⟩ |
| /b/ | ⟨b⟩ |
| /t/ | ⟨t⟩ |
| /d/ | ⟨d⟩ |
| /k/ | ⟨k⟩ |
| /g/ | ⟨g⟩ |
| /h/ | ⟨h⟩ |
| /s/ | ⟨s⟩ |
| /ɕ/ | ⟨c⟩ |
| /v/ | ⟨v⟩ |
| /m/ | ⟨m⟩ |
| /n/ | ⟨n⟩ |
| /r/ | ⟨r⟩ |
| /j/ | ⟨y⟩ |

**Conditions:** G-ORTH-001–003 override the general table where applicable. Conditioned phonetic realizations such as [ɾ] and [ŋ] do not receive separate graphemes. The inherited ⟨ci⟩ spelling of open-syllable 2.NONPAST [tɕi] under G-ORTH-002 is an additional morphophonemic exception to strict phonemic transparency.

**Depends on:** G-PHON-001 G-PHON-002 G-ORTH-001 G-ORTH-002 G-ORTH-003

### G-ORTH-005 — Capitalization, punctuation, and word division

**Statement:** Orthographic sentences capitalize the sentence-initial word and proper names. Conventional modern punctuation is used. Independent grammatical words are separated by spaces, while affixes are written attached to their hosts.

**Conditions:** Specialized conventions for compounds and any future clitic classes remain **UNSPECIFIED** until those constructions are established.

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

### G-MORPH-006 — Semantic-primal vowel-grade stems

**Statement:** The inherited semantic-primal root class forms stems by combining a consonantal root with one of four vowel grades.

| Grade vowel | Value | Example with *h SAY |
| --- | --- | --- |
| /a/ | NONFINITE | ha ‘to say’ |
| /u/ | REALIS | hu- |
| /i/ | IRREALIS | hi- |
| /e/ | LINKING | he- |

**Conditions:** The established test roots include *h SAY/UTTER and *r MOVE/TURN; thus ra is the nonfinite ‘to go’. The broader lexical inventory of the semantic-primal class is not enumerated here. The exact constructional distribution of the NONFINITE, IRREALIS, and LINKING grades beyond the values stated above remains **UNSPECIFIED**.

### G-MORPH-007 — Inherited semantic-primal person–tense template

**Statement:** Finite REALIS forms of the inherited semantic-primal conjugation use the underlying template ROOT-u-(ASSERT)-PERSON-TENSE. The inherited person consonants are *-k- ‘1’, *-t- ‘2’, and *-p- ‘3’. The tense vowels are *-i NONPAST and *-a PAST.

**Synchronic analysis:** Person and tense remain morphologically segmentable, but inherited sound change and analogy create fused surface allomorphs.

| Person | NONPAST | PAST |
| --- | --- | --- |
| 1 | -ci /ɕi/ | -va /va/ |
| 2 | -ci [tɕi] in an open syllable; /ɕi/ in a closed syllable | -da /da/ |
| 3 | -i /i/ | -va /va/ |

**Conditions:** The 1~2 NONPAST overlap reflects G-PHON-012, with [tɕ] retained for historical *-ti in open syllables. The 3.NONPAST zero-consonant outcome reflects G-PHON-019. The 1=3 PAST syncretism reflects conditioned phonetic convergence followed by analogical leveling under G-PHON-023. This conjugation is an inherited class restricted to semantic-primal roots; it is not the default conjugation of ordinary polysyllabic verbs.

**Depends on:** G-MORPH-006 G-PHON-012 G-PHON-019 G-PHON-023

### G-MORPH-008 — Inherited ASSERT/EMPH morphology

**Statement:** An inherited assertive morpheme *-h- occupies the slot after REALIS /u/ and before the person consonant in the semantic-primal finite template. Its core synchronic function is emphatic assertion, with contextual emphatic or counterexpectational force.

**Etymology:** The morpheme derives historically from *h SAY/UTTER, but the grammatical marker and lexical root are synchronically unrelated for modern speakers.

**Allomorphy:** Historical intervocalic *h before *p, *t, or *k assimilated completely under G-PHON-022. In this paradigm the resulting protected geminates preserve all three person contrasts:

| Person | ASSERT.NONPAST | ASSERT.PAST |
| --- | --- | --- |
| 1 | -kki | -kka |
| 2 | -tti | -tta |
| 3 | -ppi | -ppa |

The geminates block the ordinary NONPAST palatalization/merger and the plain-PAST lenition/syncretism.

**Conditions:** ASSERT is established here in the REALIS finite template. Its compatibility with IRREALIS, NONFINITE, or LINKING stems remains **UNSPECIFIED**.

**Depends on:** G-MORPH-007 G-PHON-022

The inventory and ordering of verbal categories, argument-indexing exponence, TAM categories, and valency-changing affixes outside this inherited semantic-primal subsystem remain **UNSPECIFIED**.

### Derivation and compounding

### G-MORPH-005 — Productive layered derivation

**Statement:** Derivational morphology is highly productive and may stack compositionally. Productivity may vary by semantic or lexical domain, and older derived formations may become semantically opaque or morphophonologically irregular.

**Depends on:** G-MORPH-002 G-MORPH-003 G-MORPH-004

### Paradigms

The inherited semantic-primal REALIS paradigm established by G-MORPH-007–008 includes the following SAY forms:

| Underlying form | Surface form | Value |
| --- | --- | --- |
| *h-u-k-i | huci /ˈhuɕi/ | SAY.REAL-1-NPST |
| *h-u-t-i | huci [ˈhutɕi] when open | SAY.REAL-2-NPST |
| *h-u-p-i | hui /hui/ | SAY.REAL-3-NPST |
| *h-u-k-a | huva /ˈhuva/ | SAY.REAL-1-PST |
| *h-u-t-a | huda /ˈhuda/ | SAY.REAL-2-PST |
| *h-u-p-a | huva /ˈhuva/ | SAY.REAL-3-PST |
| *h-u-h-k-a | hukka [ˈhukːa] | SAY.REAL-ASSERT-1-PST |
| *h-u-h-t-a | hutta [ˈhutːa] | SAY.REAL-ASSERT-2-PST |
| *h-u-h-p-a | huppa [ˈhupːa] | SAY.REAL-ASSERT-3-PST |

The same inherited person–tense exponents apply to other semantic-primal roots, including *r MOVE/TURN: ruci, ruci, rui in the plain NONPAST and ruva, ruda, ruva in the plain PAST.

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

The inherited semantic-primal root class is established morphologically under G-MORPH-006. Canonical lexical entries in `lexicon.tsv`, the full membership of that class, and broader lexical/POS classification remain **UNSPECIFIED** unless separately established.

## Glossing conventions

Examples must follow the Leipzig Glossing Rules. Standard Leipzig abbreviations are built into `scripts/validate.py` and need not be repeated here.

### Project-specific gloss abbreviations

Add only abbreviations not covered by the Leipzig standard list.

| Abbreviation | Meaning | Notes |
| --- | --- | --- |
| ASSERT | assertive/emphatic | Core emphatic assertion; may have counterexpectational force. |
| LNK | linking grade | Semantic-primal /e/ stem grade. |
| NFIN | nonfinite | Semantic-primal /a/ stem grade. |
| NPST | nonpast | Contrasts with PST in the inherited semantic-primal conjugation. |
| REAL | realis | Semantic-primal /u/ stem grade. |

## Variation and diachrony

Diachrony is modeled selectively. Explicit historical developments may be added when they explain important structural asymmetries, irregularities, or lexicalized morphology; otherwise a plausible historical motivation may remain implicit. Historical analyses do not create synchronic exceptions unless those exceptions are separately canonized.

The following sound changes are **experimental historical laws** on the `experimental` branch. They describe a proposed diachronic derivation and do not by themselves establish productive synchronic alternations.

### G-PHON-012 — Pre-/i/ palatalization with open-syllable coronal retention

**Statement:** In inherited morphology, proto *ki palatalizes and simplifies to /ɕi/. Proto *ti palatalizes to [tɕi] and retains the affricated realization when it heads an open syllable; when the syllable is closed, it further simplifies to /ɕi/.

**Historical paths:** *ki > *tɕi > /ɕi/; *ti > [tɕi] / open syllable; *ti > *tɕi > /ɕi/ / closed syllable.

**Conditions:** The open-syllable [tɕi] reflex is phonologically conditioned and applies wherever this inherited *ti sequence heads an open syllable unless another established historical rule overrides it. In the semantic-primal conjugation, both 1.NONPAST /ɕi/ < *ki and 2.NONPAST [tɕi] ~ /ɕi/ < *ti are written ⟨ci⟩ under G-ORTH-002. Geminates created by G-PHON-022 are protected from this change.

**Ordering:** G-PHON-022 precedes this rule in forms containing historical intervocalic *hC. This rule otherwise precedes G-PHON-018, so eligible singleton *ki/*ti sequences undergo palatalization before surviving stops participate in gradation.

**Depends on:** G-ORTH-002 G-PHON-022

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

**Conditions:** Proto *p not targeted by a word-edge law remains /p/, including *p that is word-medial because of surrounding morphological material. The ordering of G-PHON-015 relative to G-PHON-012–014 is not contrastive in the currently specified environments. Whether any resulting /h ~ p ~ s/, /k ~ ɕ/, or /t ~ tɕ ~ ɕ/ alternations outside the established inherited semantic-primal forms are synchronically productive is **UNSPECIFIED**.

### G-PHON-018 — Historical stress-conditioned strong–weak gradation

**Statement:** In eligible stem-internal intervocalic position, proto *p, *t, and *k retained their strong stop grade before a stressed vowel and developed the weak grades /v d g/ before an unstressed vowel.

**Historical paths:** *p > *b > *β > /v/; *t > /d/; *k > /g/ in the weak environment. Strong *p, *t, and *k were retained.

**Conditions:** This stress-conditioned distribution is the historical source of modern G-PHON-009. Subsequent morphological reanalysis made construction- or suffix-selected grade primary synchronically. The word-edge *p changes in G-PHON-013–015 occupy separate environments.

**Ordering:** G-PHON-012 precedes this gradation, so eligible proto *ki and *ti sequences undergo their conditioned pre-/i/ palatalization outcomes before surviving velars and coronals participate in gradation.

**Depends on:** G-PHON-012

### G-PHON-019 — Historical extra-weak labial deletion

**Statement:** In selected older morphology, weak-grade /v/ in an unstressed intervocalic environment could delete, producing the extra-weak labial grade ∅.

**Conditions:** Deletion applied only where the resulting vowel sequence was licensed by the phonotactics of the relevant historical stage; otherwise /v/ was retained. In the semantic-primal conjugation, *-p-i first lenited to *-v-i and then lost /v/ after REALIS /u/ because /ui/ is a licensed nucleus, yielding 3.NONPAST -i. Corresponding deletion before PAST /a/ is blocked because /ua/ is not a canonical diphthong. The modern zero grade is inherited and nonproductive under G-PHON-016.

**Depends on:** G-PHON-006 G-PHON-016 G-PHON-018

### G-PHON-020 — Historical extra-weak coronal rhotacism

**Statement:** In selected older morphology, weak-grade /d/ underwent further intervocalic lenition through *[ð̞] and *[ɾ], after which the tap merged phonemically with /r/.

**Historical path:** *d > *[ð̞] > *[ɾ] > /r/.

**Conditions:** The resulting /r/ participates in the general modern allophony of G-PHON-017. The extra-weak coronal grade is inherited and nonproductive under G-PHON-016.

**Depends on:** G-PHON-016 G-PHON-017 G-PHON-018

### G-PHON-021 — Historical extra-weak velar gliding

**Statement:** In selected older morphology, weak-grade /g/ underwent further palatal lenition before /i e/, ultimately yielding /j/.

**Historical path:** *g > *[ɣʲ] > *[j] / _{i,e}.

**Conditions:** The original front-vowel conditioning was later morphologized. In inherited modern paradigms the extra-weak /j/ may therefore occur before any vowel and is written ⟨ğ⟩ under G-ORTH-003. This grade is nonproductive under G-PHON-016.

**Ordering:** G-PHON-012 precedes G-PHON-018 and this change; ordinary proto *ki therefore undergoes the earlier palatalization specified by G-PHON-012 rather than first becoming *gi or /j/. Proto *ti follows the open/closed-syllable outcomes of G-PHON-012. Any lexical exception must be separately established.

**Depends on:** G-PHON-012 G-PHON-016 G-PHON-018 G-ORTH-003

### G-PHON-022 — Historical intervocalic *h-stop assimilation

**Statement:** Historical intervocalic *h immediately before *p, *t, or *k assimilated completely to the following stop.

**Historical law:** *VhCV > *VCCV, where C = *p, *t, *k.

**Representation:** The resulting sequences are structurally heterosyllabic /p.p t.t k.k/ and are phonetically long [pː tː kː]; consonant length is not thereby established as an independent phonemic contrast.

**Conditions:** This was a general historical intervocalic sound change, not a rule created specifically for ASSERT morphology. The inherited ASSERT construction preserves its effects particularly transparently. Resulting geminates resist the singleton palatalization and lenition processes that create the plain semantic-primal person syncretisms.

**Ordering:** This rule precedes G-PHON-012 and G-PHON-018.

**Depends on:** G-PHON-004

### G-PHON-023 — Historical plain-PAST person convergence

**Statement:** In the inherited semantic-primal REALIS PAST, the historical 1-person *-k-a and 3-person *-p-a sequences underwent conditioned lenition after /u/ and became phonetically similar enough for analogical leveling to merge both as modern -va. Historical 2-person *-t-a yields -da.

**Conditions:** The 1=3 merger is the combined result of phonetic convergence and paradigm analogy rather than a fully regular general sound law. The exact intermediate phonetic realization of the lenited velar before analogical leveling is **UNSPECIFIED**. Geminates created by G-PHON-022 do not participate, preserving ASSERT.PAST -kka, -tta, and -ppa.

**Depends on:** G-PHON-018 G-PHON-022

## Open questions

The following matters remain **UNSPECIFIED** after the phonology/phonotactics design pass:

- the explicit sequence-specific contraction outputs for morphologically created non-diphthong vowel pairs;
- the output of nasal place assimilation before placeless /h/;
- the non-nasal segment-specific mappings used by assimilation and fusion/contraction, and the deletion target used as last-resort morpheme-boundary repair;
- the membership of actual suffixes in the neutral, self-stressing, and pre-stressing classes, and their construction-specific STRONG/WEAK grade selection;
- specialized word-division conventions for compounds and any future clitic classes;
- POS inventory and lexical entries outside the grammaticalized semantic-primal test system;
- affix forms, morpheme-order templates, and paradigms outside G-MORPH-006–008;
- case inventory and the formal realization of active–stative / ergative–absolutive alignment;
- semantic conditioning of the active–stative split;
- verbal indexing categories and their ordering/exponence outside the inherited semantic-primal person system;
- conditioning of differential case and indexing;
- predicate-class membership and copular distribution;
- valency-changing morphemes and ditransitive argument structure;
- discourse rules for constituent-order flexibility and argument omission;
- negation, interrogation, coordination, subordination, relative clauses, and other constructions outside phases 0–3.

Regression examples are maintained for the established semantic-primal REALIS person–tense and ASSERT constructions. Connected-text testing remains deferred where it would require case, argument-indexing, discourse, or other constructions that are still **UNSPECIFIED**.
