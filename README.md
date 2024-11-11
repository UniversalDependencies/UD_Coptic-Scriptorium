# Summary

UD Coptic contains manually annotated Sahidic Coptic texts, including Biblical texts, sermons, letters, and hagiography.

# Introduction

The Coptic Universal Dependency Treebank is a manually annotated corpus of Sahidic Coptic texts, currently containing excerpts from the Sahidic New Testament Gospel of Mark, Works by Archmandrite Shenoute of Atripe, the Letters of Besa, lives of Sts. Cyrus and Onnophrius, Epistle of Pseudo-Ephrem, the Dormition of John the Apostle and short stories from the Apophthegmata Patrum (Sayings of the Desert Fathers). Detailed information about the treebank is available here:

http://copticscriptorium.org/treebank.html

The data was digitized or previously available in digital format, and annotated manually for part of speech in the project Coptic Scriptorium. For individual credit and further information see:

http://copticscriptorium.org/

Coptic POS tags come from the Coptic Scriptorium tag set, which is available from the project and treebank websites.

# Further details

## Basic statistics
|      subcorpus            |        documents            | tokens  |
| ------------------------- | --------------------------- | ------- |
| Not Because a Fox Barks   | MONB XH204-216              |   2,545 |
| Abraham our Father        | MONB XL93-94, YA518-520     |   1,197 |
| Acephalous Work 22        | MONB YA421-428              |   1,699 |
| I See Your Eagerness      | MONB GF31-32                |     439 |
| Epistle of Pseudo-Ephrem  | psephrem.letter             |   1,925 |
| Gospel of Mark            | Chapters 1 - 9              |  10,810 |
| 1 Corinthians             | Chapters 1 - 7              |   4,809 |
| Book of Ruth              | Chapters 1 - 4 (complete)   |   3,470 |
| Letters of Besa           | #1,2,13,15,25               |   3,936 |
| Life of Cyrus             | life.cyrus.01               |   1,962 |
| Life of Onnophrius        | life.onnophrius.01          |   2,745 |
| Apophthegmata Patrum      | #1-6,18-19,23-32,114-139    |   4,153 |
| Martyrdom of St. Victor   | Chapters 1 - 6              |   1,986 |
| Dormition of John         | dormition.john.mercad       |   3,064 |
| Pseudo-Athanasius         | mercy_judgment              |   2,782 |
| Proclus Homilies          | #13 On Easter               |   2,344 |
| Pseudo-Flavianus          | Part 1 of 2                 |   3,537 |
| Life of John the Kalybites| Part 1 of 2                 |   3,694 |
|                           | Total:                      |  57,097 |

## Tokenization

Coptic was originally written in scriptio continua, without spaces, and modern conventions fuse multiple tokens into so-called bound groups, collapsing clitic pronouns, prepositions and other morphemes into single orthographic units.

The Coptic Treebank now annotates these bound groups as 'multi-word' tokens. However, morphological units below the POS level, including affixes and fused compounds (incorporation), are now annotated in the treebank in the MISC column, using an attribute `MSeg=A-B-C`, where A, B and C are constituent morphemes of a complex word. There is also a further attribute in the MISC column, called Orig, which appears whenever normalization has taken place and renders the word form as it appeared in the original manuscript. This can include removal of optional diacritics and contracted forms of nomina sacra, which appear expanded in the word form column.

Note that for some fused forms carrying multiple parts of speech, the native Coptic POS tag set assigns portmanteau tags, such as APST_PPERS (auxiliary, past, fused with a subject personal pronoun). In the UD guidelines for Coptic, these forms are tolerated by always selecting the argument as the function-determining unit. Thus APST_PPERS, the past auxiliary with fused pronoun, is attached as *nsubj*, ignoring the *aux* dependency. In a future version, we are considering integrating a more subtle analysis using enhanced dependencies.

For more information on Coptic tokenization, see the Coptic Scriptorium website.

## Entities and Wikification

The data contains full annotation of typed named and non-named entities, using the same ten entity types as UD_English-GUM:

  * abstract
  * animal
  * event
  * object
  * organization
  * person
  * place
  * plant
  * substance
  * time

These annotations appear in the MISC column and are bracketed in the conllua convention described by [Universal Anaphora](https://universalanaphora.org/) and the [CorefUD](https://ufal.mff.cuni.cz/corefud) format. Named entities for which corresponding Wikipedia articles exist are also suffixed with a Wikification identifier corresponding to the title of their Wikipedia page, as seen for example for Alexandria and Wadi El-Natrun in the following example:

```CoNLL-U
# newdoc id = apophthegmata.patrum:AP.019.n161.presbyter
# global.Entity = etype-identity
# sent_id = apophthegmata_patrum-AP_019_n161_presbyter_s0001
# text_en = He went once, that is the presbyter of Scetis, to the archbishop of Alexandria
# text = ⲁϥⲃⲱⲕ ⲛⲟⲩⲟⲉⲓϣ ⲛϭⲓⲡⲉⲡⲣⲉⲥⲃⲩⲧⲉⲣⲟⲥ ⲛϣⲓⲏⲧ ϣⲁⲡⲁⲣⲭⲏⲉⲡⲓⲥⲕⲟⲡⲟⲥ ⲛⲣⲁⲕⲟⲧⲉ .
1-3	ⲁϥⲃⲱⲕ	_	_	_	_	_	_	_	_
1	ⲁ	ⲁ	AUX	APST	_	3	aux	_	Orig=Ⲁ
2	ϥ	ⲛⲧⲟϥ	PRON	PPERS	Definite=Def|Gender=Masc|Number=Sing|Person=3|PronType=Prs	3	nsubj	_	_
3	ⲃⲱⲕ	ⲃⲱⲕ	VERB	V	VerbForm=Fin	0	root	_	_
4-5	ⲛⲟⲩⲟⲉⲓϣ	_	_	_	_	_	_	_	_
4	ⲛ	ⲛ	ADP	PREP	_	5	case	_	_
5	ⲟⲩⲟⲉⲓϣ	ⲟⲩⲟⲉⲓϣ	NOUN	N	_	3	obl	_	Orig=ⲟⲩⲟ̇ⲉⲓ̇ϣ
6-8	ⲛϭⲓⲡⲉⲡⲣⲉⲥⲃⲩⲧⲉⲣⲟⲥ	_	_	_	_	_	_	_	_
6	ⲛϭⲓ	ⲛϭⲓ	PART	PTC	_	8	case	_	Orig=ⲛ̇ϭⲓ̇
7	ⲡⲉ	ⲡ	DET	ART	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	8	det	_	Entity=(person
8	ⲡⲣⲉⲥⲃⲩⲧⲉⲣⲟⲥ	ⲡⲣⲉⲥⲃⲩⲧⲉⲣⲟⲥ	NOUN	N	Foreign=Yes	3	dislocated	_	OrigLang=grc
9-10	ⲛϣⲓⲏⲧ	_	_	_	_	_	_	_	_
9	ⲛ	ⲛ	ADP	PREP	_	10	case	_	Orig=ⲛ̇
10	ϣⲓⲏⲧ	ϣⲓⲏⲧ	PROPN	NPROP	_	8	nmod	_	Entity=(place-Wadi_El_Natrun)person)|Orig=ϣⲓ̇ⲏⲧ
11-13	ϣⲁⲡⲁⲣⲭⲏⲉⲡⲓⲥⲕⲟⲡⲟⲥ	_	_	_	_	_	_	_	_
11	ϣⲁ	ϣⲁ	ADP	PREP	_	13	case	_	_
12	ⲡ	ⲡ	DET	ART	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	13	det	_	Entity=(person
13	ⲁⲣⲭⲏⲉⲡⲓⲥⲕⲟⲡⲟⲥ	ⲁⲣⲭⲏⲉⲡⲓⲥⲕⲟⲡⲟⲥ	NOUN	N	Foreign=Yes	3	obl	_	Orig=ⲁⲣⲭⲏⲉ̇ⲡⲓ̇ⲥⲕⲟⲡⲟⲥ|OrigLang=grc
14-15	ⲛⲣⲁⲕⲟⲧⲉ	_	_	_	_	_	_	_	_
14	ⲛ	ⲛ	ADP	PREP	_	15	case	_	Orig=ⲛ̇
15	ⲣⲁⲕⲟⲧⲉ	ⲣⲁⲕⲟⲧⲉ	PROPN	NPROP	_	13	nmod	_	Entity=(place-Alexandria)person)
16	.	.	PUNCT	PUNCT	_	3	punct	_	Orig=·ⲻ
```

## Cxn

We use the MISC field `Cxn` annotation to distinguish some complex constructions in a Construction Grammar (CxG) framework developed by collaborators from [Dagstuhl Seminar 23191](https://www.dagstuhl.de/en/seminars/seminar-calendar/seminar-details/23191) for the integration of CxG analyses into UD trees. Construction labels are always attached to the highest token belonging to the necessary or defining elements of the construction, and carry hierarchical designations, such as a prefix `Cxn=Conditional` for all conditional constructions, but a more specific `Cxn=Conditional-NegativeEpistemic` for negative epistemic conditionals (the unrealized type seen in "if one had, then one would have"). Individual elements of a construction, such as the Protasis or the Apodosis are annotated using the `CxnElt` MISC annotation. For more information and for work using these annotations, please refer to [Weissweiler et al. 2024](https://aclanthology.org/2024.lrec-main.1471).

# Acknowledgments

The underlying POS tagged material was produced as part of the projects Coptic Scriptorium, KOMeT and KELLIA, funded by the NEH in the USA and BMBF and DFG in Germany (see http://copticscriptorium.org/ for more details). Treebank annotation was done mainly by Mitchell Abrams, Liz Davidson and Amir Zeldes. Thanks are also due to Israel Avrahamy, Asael Benyami, Yinon Kahan and Oran Szachter for their contributions.

# Data Splits

Dataset splits attempt to balance genres across all sets, as well as preserve contiguous documents whenever possible. Sentence and document IDs in the data indicate the respective source texts. Sentences are not shuffled.

# References

To cite the treebank please refer to the following paper:

  * Zeldes, Amir & Abrams, Mitchell (2018). "The Coptic Universal Dependency Treebank". In: *Proceedings of the Universal Dependencies Workshop 2018*. Brussels, Belgium, 192-201.

```bibtex
@InProceedings{ZeldesAbrams2018,
  author    = {Amir Zeldes and Mitchell Abrams},
  title     = {The {C}optic {U}niversal {D}ependency {T}reebank},
  booktitle = {Proceedings of the Universal Dependencies Workshop 2018},
  pages     = {192--201},
  year      = {2018},
  address   = {Brussels}
}
```

Further information on relevant annotation standards and NLP tools used prior to manual correction can be found in these papers:

  * Zeldes, Amir & Schroeder, Caroline T. (2016a). SCRIPTORIUM Part-of-Speech Tagsets for Sahidic Coptic. Georgetown University and University of the Pacific, Technical Report.
  * Zeldes, Amir & Schroeder, Caroline T. (2016b). "An NLP Pipeline for Coptic". In: Proceedings of LaTeCH 2016 - The 10th SIGHUM Workshop at the Annual Meeting of the ACL. Berlin, 146-155.

# Changelog

  * CHANGELOG 2.14 -> 2.15

Changed :npmod subtype to :unmarked; added UCxn annotations; minor corrections.

  * CHANGELOG 2.13 -> 2.14

Added nmod:poss for possessive determiners and changed xpos IMOD to NOUN + obl:npmod instead of ADV + advmod; minor corrections.

  * CHANGELOG 2.12 -> 2.13

Added 1 Corinthians 7

  * CHANGELOG 2.11 -> 2.12

Added document author, work, source and URN metadata; numerous minor corrections.

  * CHANGELOG 2.10 -> 2.11

Added the Life of John the Kalybites, part 1, to training partition; punctuation attachment now using udapi; numerous minor corrections.

  * CHANGELOG 2.9 -> 2.10

Added `acl` vs. `acl:relcl` distinction; Renamed `Morph` to `MSeg` to match other UD corpora; Systematic fixes to xcomp with object; Minor corrections.

  * CHANGELOG 2.8 -> 2.9

Added Pseudo-Flavianus to train, minor corrections.

  * CHANGELOG 2.7 -> 2.8

Added `Foreign` feature and `OrigLang` annotation in MISC for loanwords

  * CHANGELOG 2.6 -> 2.7

Added Proclus of Cyzicus Homily 13, On Easter. Nested named and non-named entity annotations have been added to the entire corpus.

  * CHANGELOG 2.5 -> 2.6

Added Discourse of Pseudo-Athanasius on Mercy and Judgment, numerous corrections and consistency checks to (especially auxiliary) lemmas

  * CHANGELOG 2.4 -> 2.5

Added Besa's Letters 1-2 (On Vigilance, Exhortations), Excerpt from Shenoute's I See Your Eagerness, Life of Cyrus, Life of Onnophrius, Epistle of Pseudo-Ephrem, Dormition of John and Apophthegmata Patrum 114-139, numerous corrections and stabilized splits. 

The corpus is now larger than 30K word forms, and train/dev/test splits should now be stable, with only the train partition growing.

  * CHANGELOG 2.3 -> 2.4

Added Mark 7-9. Rearranged documents in train/dev/test so that documents and parts of larger works are contiguous and genre balance is maintained. Negative polarity added for negative auxiliaries, deprel obl:npmod added for non-prepositional adverbial NPs (formerly part of advmod).

  * CHANGELOG 2.2 -> 2.3

Added new documents: Shenoute's Acephalous Work 22 (YA421-428) and Abraham our Father (XL93-94, YA518-520), the Martyrdom of St. Victor Chapters 1-6, Apophthegmata Patrum 27-32, 1 Corinthians Chapters 3-6 (corpus now includes 1-6) and Mark 6 (corpus now includes 1-6). Rearranged documents in train/dev/test so that all documents are contiguous and genre balance is improved (all sets now include different Shenoute texts). 

Also added MISC attributes: Morphs (for sub-word morphological segmentation) and Orig (records unnormalized word form where normalization has been carried out)

  * CHANGELOG 2.1 -> 2.2

Repository renamed from UD_Coptic to UD_Coptic-Scriptorium. Added 1 Corinthians 1-3, rearranged material from Mark to make contiguous documents in train/dev/test.

  * CHANGELOG 2.0 -> 2.1

Added Apophthegmata Patrum (AP) 1-4 to training data and moved AP24 to dev and AP26 to test to create contiguous document partitions for the AP portions.

  * CHANGELOG 1.4 -> 2.0

Switched to UD v2 and added bound group information (multiword super-tokens). Added Gospel of Mark chapters 3-5 to previously available dev data, and numerous error corrections.

  * CHANGELOG 1.3 -> 1.4

First inclusion in full release as of v1.4. Added Gospel of Mark chapter 2 to previously available dev data, and numerous error corrections.

=== Machine readable metadata ==============

Documentation status: complete
Data source: manual
Data available since: UD v1.4
License: CC BY 4.0
Includes text: yes
Lemmas: manual native
UPOS: converted from manual
XPOS: manual native
Features: automatic
Relations: manual native
Genre: bible fiction nonfiction
Contributors: Abrams, Mitchell; Davidson, Elizabeth; Zeldes, Amir
Contributing: elsewhere
Contact: amir.zeldes@georgetown.edu

============================================