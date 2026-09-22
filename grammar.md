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

**Statement:** /m n/ may assimilate in place of articulation before a following place-bearing consonant, but assimilation is limited rather than automatic in every preconsonantal environment. Placeless /h/ does not trigger nasal place assimilation: /mh/ and /nh/ retain the nasal's underlying place.

**Conditions:** The place-bearing consonants and morphological or prosodic domains that trigger nasal assimilation, and the resulting outputs before those consonants, remain **UNSPECIFIED**.

### Phonotactics

### G-PHON-004 — Syllable template

**Statement:** Canonical syllables have the shape `(C)V(C)`. Consonant clusters are not permitted within a syllable.

**Conditions:** A nucleus may contain one vowel phoneme or one canonical diphthong. Onset distribution beyond the explicitly restricted consonants is **UNSPECIFIED**.

### G-PHON-006 — Diphthong inventory

**Statement:** The canonical diphthongs are /ai ei ui/.

**Conditions:** These diphthongs constitute single heavy syllable nuclei for stress. Morphologically created /ua/ is exceptionally preserved as hiatus /u.a/ under G-PHON-012. Whether non-diphthong vowel sequences, including /ua/, may occur lexically is **UNSPECIFIED**. Other morphologically created vowel sequences are repaired under G-PHON-011 and G-PHON-012.

### G-PHON-007 — Position-sensitive coda inventory

**Statement:** Medial codas permit /p b t d k g m n r s/. Word-final codas permit /t k n r s/. No other consonants occur in coda position.

**Depends on:** G-PHON-004

### G-PHON-008 — Onset-only consonants

**Statement:** /h ɕ j/ occur only in onset position and are prohibited in codas. /j/ occurs only before a vowel.

**Conditions:** Because G-PHON-007 exhaustively defines coda inventories, /v/ is also excluded from codas. Further restrictions on word-initial versus word-medial onsets are **UNSPECIFIED**.

**Depends on:** G-PHON-004 G-PHON-007

### Prosody

### G-PHON-005 — Weight-sensitive stress

**Statement:** Closed syllables, syllables containing /ai ei ui/, and contraction products explicitly marked heavy by G-PHON-012 are heavy. Stress falls on the penultimate syllable by default; a heavy final syllable attracts final stress.

**Conditions:** Morphological suffix classes may override the phonological default by being stress-attracting or stress-neutral. The membership and behavior of those suffix classes are **UNSPECIFIED** until the relevant morphology is established. Contraction-class dominance under G-PHON-012 does not by itself imply stress attraction.

**Depends on:** G-PHON-006 G-PHON-007 G-PHON-012

## Morphophonology

### G-PHON-011 — Morpheme-boundary repair hierarchy

**Statement:** When morphology creates an illicit consonant or vowel sequence, repair applies in the order assimilation > fusion/contraction > deletion. The highest-ranked available process that yields a phonotactically legal output applies. Epenthesis is not part of the default repair hierarchy.

**Conditions:** Nasal assimilation is governed by G-PHON-010; vowel repair by G-PHON-012; non-nasal consonant assimilation by G-PHON-013; consonant fusion and preservation by G-PHON-014; and last-resort deletion by G-PHON-015.

**Depends on:** G-PHON-004 G-PHON-006 G-PHON-007 G-PHON-010 G-PHON-012 G-PHON-013 G-PHON-014 G-PHON-015

### G-PHON-012 — Sequence-specific vowel repair

**Statement:** Morphologically created adjacent vowels are repaired by the following sequence-specific mappings. Canonical /ai ei ui/ remain diphthongs and are not repaired.

| Input | Output | Prosody/conditioning |
| --- | --- | --- |
| /ii/ | /i/ | contracted nucleus remains heavy |
| /ee/ | /e/ | contracted nucleus remains heavy |
| /aa/ | /a/ | contracted nucleus remains heavy |
| /uu/ | /u/ | contracted nucleus remains heavy |
| /ia/ | /ja/ | /i/ glides to /j/ |
| /iu/ | /ju/ | /i/ glides to /j/ |
| /eu/ | /ju/ | via /eu/ > /iu/ > /ju/ |
| /au/ | /u/ | contracted nucleus remains heavy |
| /ue/ | /ui/ | yields the canonical heavy diphthong /ui/ |
| /ua/ | /u.a/ | hiatus is preserved; no contraction |

The three morphologically conditioned sequences /ie ea ae/ are resolved by boundary type and suffix class:

| Input | Directional prefix + root | Dominant/fusing suffix | Recessive/transparent suffix |
| --- | --- | --- | --- |
| /ie/ | /je/ | /e/ | /je/ |
| /ea/ | not applicable to the established directional prefixes | /a/ | /e/ |
| /ae/ | /e/ with retained heavy weight | /e/ with retained heavy weight | /a/ |

**Conditions:** At a directional-prefix + root boundary, repair preserves the root vowel where possible: /i-e/ > /je/ and /a-e/ > heavy /e/. At a stem + suffix boundary, a dominant/fusing suffix controls the resulting vowel in /ie ea ae/, while a recessive/transparent suffix preserves the stem vowel where possible. The tense suffix layer is dominant/fusing; this classification is independent of stress attraction unless a separate prosodic rule states otherwise. Membership of other suffixes in the dominant/fusing versus recessive/transparent contraction classes remains **UNSPECIFIED**.

**Depends on:** G-PHON-005 G-PHON-006 G-MORPH-010 G-MORPH-012

### G-PHON-013 — Non-nasal consonant assimilation

**Statement:** The default non-nasal boundary-assimilation directions are regressive voicing and progressive place: where an applicable sequence supports those features, the left consonant copies the right consonant's voicing and the right consonant copies the left consonant's place. More specific mappings below override this default.

**Conditions:** For oral stop + oral stop sequences /p b t d k g/, only voicing assimilates regressively; both stops retain their places. A consonant before placeless /h/ does not assimilate to /h/. In /hC/, /h/ totally assimilates to the following consonant, producing /CC/ when that sequence can be syllabified legally. /j/ before a consonant does not assimilate and cannot survive there under G-PHON-008; it therefore proceeds to deletion if no higher-ranked repair applies.

**Depends on:** G-PHON-002 G-PHON-007 G-PHON-008 G-PHON-011

### G-PHON-014 — Consonant fusion and heterosyllabic preservation

**Statement:** Identical consonants created by morphology or assimilation are not automatically degeminated: /CC/ is preserved heterosyllabically when the first consonant is a legal coda and the second a legal onset. Selected non-identical sequences instead undergo fusion.

**Conditions:** The selected fusion mappings are:

- /sɕ/ and /ɕs/ fuse to /ɕ/ before /i/, and to /s/ elsewhere.
- /ts ds tɕ dɕ/ arising from /t d/ + /s ɕ/ surface respectively as [ts dz tɕ dʑ]. These affricates are boundary-fusion outputs, not additional phonemes.
- In the reverse order, /s ɕ/ + /t d/ is preserved across a syllable boundary whenever phonotactics permit it. Because /ɕ/ is onset-only, /ɕt/ and /ɕd/ cannot be preserved with /ɕ/ as a coda and continue through the repair hierarchy.
- /CC/ created by /hC/ assimilation under G-PHON-013 likewise survives if heterosyllabification is legal.

**Depends on:** G-PHON-002 G-PHON-007 G-PHON-008 G-PHON-011 G-PHON-013

### G-PHON-015 — Last-resort boundary deletion

**Statement:** Deletion applies only when assimilation and fusion/contraction cannot yield a legal output. A segment whose positional restrictions make it structurally illegal is deleted before an unrestricted segment. If both members are equally legal, the left member of the boundary sequence—normally the stem-final segment before a suffix—is deleted, preserving the right member.

**Conditions:** This makes /j/ the deletion target before a consonant, because /j/ occurs only before vowels. It likewise favors deletion of /ɕ/ or /v/ when either would otherwise have to occupy an illegal coda. If neither member has a stronger positional restriction, C₁+C₂ > C₂ as the final fallback.

**Depends on:** G-PHON-007 G-PHON-008 G-PHON-011

### G-PHON-016 — Syllable-conditioned reflex of inherited *-ti

**Statement:** In inherited *-ti morphology, an open-syllable reflex is written `-ci` and surfaces as [-tɕi], while a reflex followed by a coda consonant is written `-ciC` and has /-ɕiC/.

**Conditions:** The open-syllable [tɕ] is a surface affricate and does not add /tɕ/ to the phoneme inventory. The spelling `-ci` is established for this historical reflex in both environments; broader orthographic correspondences remain governed by the orthography section.

**Depends on:** G-PHON-002 G-PHON-004 G-PHON-007 G-PHON-014

The exact prosodic and morphological domains of G-PHON-009, the place-bearing triggers and outputs of G-PHON-010, the membership of non-tense suffixes in the G-PHON-012 contraction classes, and the concrete stress classes referenced by G-PHON-005 remain **UNSPECIFIED**.

## Orthography

The inherited *-ti reflex specified by G-PHON-016 is written `-ci` in an open syllable and `-ciC` before a coda consonant. Beyond this established morphophonological spelling, the grapheme inventory, general grapheme-to-phoneme correspondences, capitalization, punctuation, and word-division rules remain **UNSPECIFIED**.

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
| n | noun | Nominal lexical class. |
| v | verb | Verbal lexical class; includes stative/property concepts traditionally expressed by adjectives in some languages. |

### Nominal morphology

### G-MORPH-006 — Nominal case inventory and core alignment

**Statement:** The nominal case inventory is ABS, ERG, GEN, DAT, LOC, CONT, POS, and INS/COM. ABS marks transitive P and inactive S; ERG marks transitive A and active S. GEN marks dependency relations including possession, affiliation, and part–whole relations. DAT marks an affected personal domain. LOC marks general spatial reference, CONT marks bounded containment or inclusion, POS marks contact/configuration/position, and INS/COM marks instrumental or associative/comitative relations. ABS is zero-marked.

**Conditions:** The semantic or lexical criteria assigning intransitive S arguments to the active versus inactive class remain **UNSPECIFIED**. Differential marking conditions and the segmental forms of the overt case suffixes remain **UNSPECIFIED**.

**Depends on:** G-SYN-002 G-SYN-003

### G-MORPH-007 — Nominal inflection template

**Statement:** The nominal template is `NOUN-(NUMBER)-(GEN)-CASE`, with number optional.

**Conditions:** GEN may occur as the sole case marker or as an inner case before an eligible outer case under G-MORPH-008. Number categories and their productivity are specified by G-MORPH-015; their segmental forms remain **UNSPECIFIED**.

### G-MORPH-008 — Restricted genitive case stacking

**Statement:** GEN is the only case that productively stacks. It may precede DAT, LOC, CONT, POS, or INS/COM, yielding an inner dependency relation plus an outer clausal or semantic relation.

**Conditions:** GEN does not stack with ABS or ERG, and DAT, LOC, CONT, POS, and INS/COM do not productively stack with one another.

**Depends on:** G-MORPH-006 G-MORPH-007

### Pronominal and deictic systems

Free pronouns and bound person indexes share an older person base, but the bound indexing series is synchronically grammaticalized morphology under G-MORPH-018. The segmental forms of free pronouns, their number and clusivity distinctions, deixis, and any pronominally restricted alignment or case patterns remain **UNSPECIFIED**.

### Verbal morphology

### G-MORPH-009 — Verbal morphology template

**Statement:** The verbal template is `DIRECTIONAL-OBJ/PAT-ROOT-AUX/APP-SUBJ/AGT-TENSE-ASPECT`.

**Conditions:** The underlying person bases and alignment domains of OBJ/PAT and SUBJ/AGT indexing are specified by G-MORPH-016–017. Their differential overt-realization conditions and slot-specific surface outputs remain **UNSPECIFIED**. The auxiliary inventory is **UNSPECIFIED**. Applicative morphology occupies the AUX/APP slot as specified below.

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

**Statement:** Tense follows subject/agent indexing and precedes aspect. `-i` marks nonpast and `-a` marks past. Zero aspect marks imperfective and `-n` marks perfective. The tense suffix layer belongs to the dominant/fusing vowel-contraction class of G-PHON-012.

**Conditions:** Contraction-class dominance does not itself make a tense suffix stress-attracting. The semantic boundaries of past versus nonpast and perfective versus imperfective, including any interaction with lexical aspect, remain **UNSPECIFIED**.

**Depends on:** G-PHON-012

### G-MORPH-013 — Two applicative classes

**Statement:** Minitongue has two productive applicative classes. An affected applicative promotes a DAT participant. A general oblique applicative promotes an INS/COM, LOC, CONT, or POS participant.

**Conditions:** Each applicative is represented by one compact underlying segmental form once established; its surface variants are derived by the general morphophonology unless a separate rule establishes otherwise. The segmental forms themselves and any historical relationship between the two applicatives remain **UNSPECIFIED**. GEN is not a productive applicative input. Applicatives occupy the AUX/APP position in G-MORPH-009.

**Depends on:** G-MORPH-006 G-MORPH-009

### G-MORPH-014 — Applicative promotion and directional interaction

**Statement:** An applied participant becomes an ABS core object and is eligible for OBJ/PAT indexing. When an applicative and directional target the same underlying relation, the applicative changes argument status while the directional preserves the convergent, neutral, or divergent interpretation of that relation.

**Conditions:** The treatment, case, and indexing of any pre-existing basic object after applicativization, including possible double-object behavior, are **UNSPECIFIED**.

**Depends on:** G-MORPH-010 G-MORPH-011 G-MORPH-013 G-SYN-003 G-SYN-006

### G-MORPH-015 — Nominal number inventory

**Statement:** Nominal number distinguishes zero-marked singular, productive plural, productive collective, and an archaic/restricted dual.

**Conditions:** The dual is retained for conventional natural pairings rather than as a fully productive general number category. The precise lexical or semantic licensing of natural-pair duals and the segmental forms of PL, COLL, and DU remain **UNSPECIFIED**.

### G-MORPH-016 — Shared person-index bases

**Statement:** The bound person-index system has the underlying bases `-k-` 1P, `-t-` 2P, and `-p-` 3P. The same person bases underlie both the OBJ/PAT and SUBJ/AGT slots.

**Conditions:** Person is primary in these bound indexes; number and clusivity are not obligatorily fused into the `k/t/p` contrast. Because the two indexing slots occur in different morphological environments, regular morphophonology may produce different surface reflexes. Slot-specific allomorphy is not assumed unless the general rules fail to derive an accepted form.

### G-MORPH-017 — Alignment domains of verbal indexing

**Statement:** OBJ/PAT indexing has an absolutive/inactive domain: it indexes transitive P and inactive intransitive S. SUBJ/AGT indexing has an ergative/active domain: it indexes transitive A and active intransitive S. An applied participant promoted to ABS under G-MORPH-014 is eligible for OBJ/PAT indexing.

**Conditions:** Eligibility for an indexing domain does not require overt realization in every clause. Person, animacy, definiteness, discourse status, or other factors may condition overt realization, but those conditions remain **UNSPECIFIED**.

**Depends on:** G-MORPH-006 G-MORPH-009 G-MORPH-014 G-MORPH-016 G-SYN-002 G-SYN-003

### G-MORPH-018 — Free pronouns and bound indexes

**Statement:** Free pronouns and the bound `k/t/p` person indexes reflect a shared older person system, but the bound indexes are synchronically grammaticalized verbal morphology. Modern free pronouns need not correspond transparently or one-to-one to the bound forms.

**Conditions:** The synchronic forms and internal morphology of free pronouns remain **UNSPECIFIED**.

**Depends on:** G-MORPH-016

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

**Conditions:** The case inventory is specified by G-MORPH-006. The person-index bases and their core alignment domains are specified by G-MORPH-016–017. Case and/or overt indexing may be differential according to grammatical or semantic properties, and selected pronouns or historically older constructions may preserve distinct patterns. The conditioning hierarchy and distribution of differential marking remain **UNSPECIFIED**.

**Depends on:** G-SYN-002 G-MORPH-016 G-MORPH-017

### G-SYN-004 — Predicate-centered split predicate system

**Statement:** Verbs, including stative/property verbs, and some nouns may function directly as predicates. Property concepts conventionally expressed by adjectives in some languages are stative verbs in Minitongue; there is no separate canonical adjective lexical class.

**Exceptions:** Older copular or auxiliary constructions may survive in restricted environments once explicitly established.

**Conditions:** Stative verbs use the ordinary verbal architecture rather than a dedicated adjective/stative paradigm. Individual combinations with aspect, directionals, applicatives, or other verbal morphology are licensed by semantic compatibility. The distribution of direct nominal predication and any copular or auxiliary support remains **UNSPECIFIED**.

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

### G-LEX-001 — Layered root and citation-stem representation

**Statement:** Canonical lexical entries distinguish a synchronic morphological root from the ordinary citation stem when that distinction is structurally relevant. For verbs, `lemma` is the unindexed nonfinite a-grade citation form. For nouns, `lemma` is the case-neutral citation stem. An underlying root is stored in `features` when needed for productive morphological analysis.

**Conditions:** Ordinary root behavior is inferred from the stored form and general rules. A lexical root or morphophonological class is recorded explicitly only when behavior is not predictable. Historical reconstructions belong in `etymology`, not in the synchronic root representation. A verbal entry records its canonical lexical valency frame in `features`; the controlled machine vocabulary for those feature values remains **UNSPECIFIED** until lexical entries are added.

### G-LEX-002 — Lexical sense individuation

**Statement:** Predictable contextual and compositionally derived meanings remain within one lexical sense. A new `sense_id` is created when a meaning is lexicalized, has distinct argument structure or grammatical selection, or has materially different usage constraints.

**Conditions:** Directional, case, applicative, and other productive compositional meanings are not duplicated as lexical senses merely because they require different English translations.

### G-LEX-003 — Selective explanatory etymology

**Statement:** Lexical etymology is recorded when it explains a synchronically important alternation, asymmetry, irregularity, or morphological relationship. Transparent lexemes need not receive reconstructed histories solely for completeness.

No canonical lexical entries have yet been established.

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
- whether non-diphthong vowel sequences, including morphologically preserved /ua/, may occur lexically;
- the exact prosodic and morphological environments and phonetic outputs of intervocalic stop weakening;
- the place-bearing triggers, domains, and outputs of nasal place assimilation beyond the established non-assimilation before /h/;
- the membership of non-tense suffixes in the dominant/fusing versus recessive/transparent contraction classes;
- the identity and behavior of stress-attracting and stress-neutral suffix classes, and whether either stress class correlates with contraction-class membership;
- the entire orthographic system;
- canonical lexical entries and the controlled feature vocabulary used for lexical valency;
- overt case-suffix forms, the segmental forms of PL/COLL/DU, precise licensing of the restricted natural-pair dual, and complete paradigms;
- semantic conditioning of the active–stative split;
- differential overt-indexing conditions and the slot-specific surface reflexes of the shared `k/t/p` person bases;
- free-pronoun forms, pronominal number/clusivity, deixis, and any pronominally restricted alignment patterns;
- auxiliary inventory and behavior;
- conditioning of differential case and indexing;
- the lexical classes licensing directional GEN and whether DAT extends productively to possession, allegiance, or transfer of control;
- the segmental forms of the two applicatives, the treatment of a pre-existing object after applicativization, ditransitive argument structure, and any additional valency-changing operations;
- direct nominal-predicate behavior and copular distribution;
- discourse rules for constituent-order flexibility and argument omission;
- negation, interrogation, coordination, subordination, relative clauses, and other constructions outside phases 0–3.

Canonical regression examples are not yet added because the lexicon remains empty and the segmental forms of case suffixes, indexing markers, and applicatives remain **UNSPECIFIED**. The directional and TAM forms are established, but complete examples would still require inventing canonical lexical and inflectional material.
