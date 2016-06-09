# UD_Coptic

The Coptic Universal Dependency Treebank is a manually annotated corpus of Sahidic Coptic texts, currently containing excerpts from the Sahidic New Testament Gospel of Mark, Archmandrite Shenoute of Atripe's "Not Because a Fox Barks" and several short stories from the Apophthegmata Patrum (Sayings of the Desert Fathers). Detailed information about the treebank is available here:

https://corpling.uis.georgetown.edu/coptic-treebank/

The data was digitized and annotated manually for part of speech in the project Coptic Scriptorium. For individual credit and further information see: 

http://copticscriptorium.org/

Coptic POS tags come from the Coptic Scriptorium tag set, which is available from the project and treebank websites. The mapping to universal POS tags is described in the PDF of the treebank guidelines, also available from the website. A machine readable version of the guidelines for the UD website is currently being produced.

## Basic statistics
|      subcorpus          |        document       | tokens |
| ----------------------- | --------------------- | ------ |
| Not Because a Fox Barks | MONB_XH_204_216       |   2554 |
| Gospel of Mark          | Chapter 1             |   1221 |
| Apophthegmata Patrum    | AP.005.unid.senses    |     81 |
| Apophthegmata Patrum    | AP.006.n196.worms     |     91 |
| Apophthegmata Patrum    | AP.018.n372.anger     |     67 |
| Apophthegmata Patrum    | AP.019.presbyter      |     89 |
| Apophthegmata Patrum    | AP.023.isaac-cells.07 |     55 |
| Apophthegmata Patrum    | AP.024.isaac-cells.07 |     32 |
| Apophthegmata Patrum    | AP.025.isaac-cells.12 |     59 |
| Apophthegmata Patrum    | AP.026.cassian.07     |    112 |
|                         | Total:                |   4361 |

## Tokenization
Coptic was originally written in scriptio continua, without spaces, and modern conventions fuse multiple tokens into so-called bound groups, collapsing clitic pronouns, prepositions and other morphemes into single orthographic units.

The Coptic Treebank does not designate these bound groups and therefore contains no 'multi-unit' tokens. However, the original bound group information for the documents is available from the Coptic Scriptorium website in other formats, not merged into the conllu format at present. The same applies to morphological units below the POS level, including affixes and fused compounds.

Additionally, for some fused forms carrying multiple parts of speech, the native Coptic POS tag set assigns portmanteau tags, such as APST_PPERS (auxiliary, past, fused with a subject personal pronoun). In the UD guidelines for Coptic, these forms are tolerated by always selecting the argument as the function determining unit. Thus APST_PPERS is attached as *nsubj*, ignoring the *aux* dependency. In a future version, we plan to integrate a more subtle analysis using the conllu subtokenization notation.

For more information on Coptic tokenization, see the Coptic Scriptorium website.

## References
  * Zeldes, A. & Schroeder, C. T. (2016). SCRIPTORIUM Part-of-Speech Tagsets for Sahidic Coptic. Georgetown University and University of the Pacific, Technical Report. 

--- Machine readable metadata ---

Documentation status: complete
Data source: manual
Data available since: UD v2.0
License: CC BY 4.0
Genre: bible fiction nonfiction
Contributors: Zeldes, Amir
