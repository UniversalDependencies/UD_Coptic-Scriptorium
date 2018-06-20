# Summary

UD Coptic contains manually annotated Sahidic Coptic texts, currently from the Gospel of Mark, Shenoute of Atripe's "Not Because a Fox Barks", the Letters of Besa, and several short stories from the Apophthegmata Patrum.

# Introduction

The Coptic Universal Dependency Treebank is a manually annotated corpus of Sahidic Coptic texts, currently containing excerpts from the Sahidic New Testament Gospel of Mark, Archmandrite Shenoute of Atripe's "Not Because a Fox Barks", the Letters of Besa, and several short stories from the Apophthegmata Patrum (Sayings of the Desert Fathers). Detailed information about the treebank is available here:

https://corpling.uis.georgetown.edu/coptic-treebank/

The data was digitized and annotated manually for part of speech in the project Coptic Scriptorium. For individual credit and further information see:

http://copticscriptorium.org/

Coptic POS tags come from the Coptic Scriptorium tag set, which is available from the project and treebank websites.

# Further details

## Basic statistics
|      subcorpus          |        document       | tokens  |
| ----------------------- | --------------------- | ------- |
| Not Because a Fox Barks | MONB_XH_204_216       |   2,553 |
| Gospel of Mark          | Chapters 1 - 5        |   5,378 |
| 1 Corinthians           | Chapters 1 - 3        |   1,967 |
| Letters of Besa         | #13,15,25             |   1,980 |
| Apophthegmata Patrum    | #1-6,18-19,23-26      |   1,318 |
|                         | Total:                |  13,196 |

## Tokenization
Coptic was originally written in scriptio continua, without spaces, and modern conventions fuse multiple tokens into so-called bound groups, collapsing clitic pronouns, prepositions and other morphemes into single orthographic units.

The Coptic Treebank now annotates these bound groups as 'multi-unit' tokens. However, morphological units below the POS level, including affixes and fused compounds, are not annotated in the treebank. This information is however annotated in non-treebanked versions of the data, available from the project website. In the future we hope to merge more morphological information directly into the treebank files in the conllu format.

Additionally, for some fused forms carrying multiple parts of speech, the native Coptic POS tag set assigns portmanteau tags, such as APST_PPERS (auxiliary, past, fused with a subject personal pronoun). In the UD guidelines for Coptic, these forms are tolerated by always selecting the argument as the function-determining unit. Thus APST_PPERS, the past auxiliary with fused pronoun, is attached as *nsubj*, ignoring the *aux* dependency. In a future version, we are considering integrating a more subtle analysis using the conllu subtokenization notation.

For more information on Coptic tokenization, see the Coptic Scriptorium website.

# Acknowledgments

The underlying POS tagged material was produced as part of the projects Coptic Scriptorium, KOMeT and KELLIA, funded by the NEH in the USA and BMBF and DFG in Germany (see http://copticscriptorium.org/ for more details). Treebank annotation was done by Mitchell Abrams, Liz Davidson and Amir Zeldes.

# Data Splits

Dataset splits attempt to balance genres across all sets, as well as preserve contiguous documents whenever possible. Sentence and document IDs in the data indicate the respective source texts. Sentences are not shuffled.

# References
  * Zeldes, A. & Schroeder, C. T. (2016a). SCRIPTORIUM Part-of-Speech Tagsets for Sahidic Coptic. Georgetown University and University of the Pacific, Technical Report.
  * Zeldes, A. & Schroeder, C. T. (2016b). "An NLP Pipeline for Coptic". In: Proceedings of LaTeCH 2016 - The 10th SIGHUM Workshop at the Annual Meeting of the ACL. Berlin, 146-155.

# Changelog

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
Contributing: here
Contact: amir.zeldes@georgetown.edu

============================================