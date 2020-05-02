import sys
from collections import defaultdict

def universalize(cs_tag,line_num):
	out_tag = ""
	if cs_tag == "AAOR":
		out_tag = "AUX"
	if cs_tag == "ACAUS":
		out_tag = "AUX"
	if cs_tag == "ACOND":
		out_tag = "SCONJ"
	if cs_tag == "ACONJ":
		out_tag = "AUX"
	if cs_tag == "ADV":
		out_tag = "ADV"
	if cs_tag == "AFUTCONJ":
		out_tag = "AUX"
	if cs_tag == "AJUS":
		out_tag = "AUX"
	if cs_tag == "ALIM":
		out_tag = "SCONJ"
	if cs_tag == "ANEGAOR":
		out_tag = "AUX"
	if cs_tag == "ANEGJUS":
		out_tag = "AUX"
	if cs_tag == "ANEGOPT":
		out_tag = "AUX"
	if cs_tag == "ANEGPST":
		out_tag = "AUX"
	if cs_tag == "ANY":
		out_tag = "AUX"
	if cs_tag == "AOPT":
		out_tag = "AUX"
	if cs_tag == "APREC":
		out_tag = "SCONJ"
	if cs_tag == "APST":
		out_tag = "AUX"
	if cs_tag == "ART":
		out_tag = "DET"
	if cs_tag == "CCIRC":
		out_tag = "SCONJ"
	if cs_tag == "CCOND":
		out_tag = "SCONJ"
	if cs_tag == "CFOC":
		out_tag = "PART"
	if cs_tag == "CONJ":
		out_tag = "CONJ"
	if cs_tag == "COP":
		out_tag = "PART"
	if cs_tag == "CPRET":
		out_tag = "AUX"
	if cs_tag == "CREL":
		out_tag = "SCONJ"
	if cs_tag == "EXIST":
		out_tag = "VERB"
	if cs_tag == "FM":
		out_tag = "X"
	if cs_tag == "FUT":
		out_tag = "AUX"
	if cs_tag == "IMOD":
		out_tag = "ADV"
	if cs_tag == "N":
		out_tag = "NOUN"
	if cs_tag == "NEG":
		out_tag = "ADV"
	if cs_tag == "NOUN":
		out_tag = "NOUN"
	if cs_tag == "NPROP":
		out_tag = "PROPN"
	if cs_tag == "NUM":
		out_tag = "NUM"
	if cs_tag == "PDEM":
		out_tag = "DET"
	if cs_tag == "PINT":
		out_tag = "PRON"
	if cs_tag == "PPERI":
		out_tag = "PRON"
	if cs_tag == "PPERO":
		out_tag = "PRON"
	if cs_tag == "PPERS":
		out_tag = "PRON"
	if cs_tag == "PPOS":
		out_tag = "DET"
	if cs_tag == "PREP":
		out_tag = "ADP"
	if cs_tag == "PTC":
		out_tag = "PART"
	if cs_tag == "PUNCT":
		out_tag = "PUNCT"
	if cs_tag == "UNKNOWN":
		out_tag = "X"
	if cs_tag == "V":
		out_tag = "VERB"
	if cs_tag == "VBD":
		out_tag = "VERB"
	if cs_tag == "VIMP":
		out_tag = "VERB"
	if cs_tag == "VSTAT":
		out_tag = "VERB"
	if cs_tag == "AAOR":
		out_tag = "AUX"
	if cs_tag == "ACAUS":
		out_tag = "AUX"
	if cs_tag == "ACOND":
		out_tag = "SCONJ"
	if cs_tag == "ACOND_PPERS":
		out_tag = "PRON"
	if cs_tag == "ACONJ":
		out_tag = "AUX"
	if cs_tag == "ADV":
		out_tag = "ADV"
	if cs_tag == "AFUTCONJ":
		out_tag = "AUX"
	if cs_tag == "AJUS":
		out_tag = "AUX"
	if cs_tag == "ALIM":
		out_tag = "SCONJ"
	if cs_tag == "ANEGAOR":
		out_tag = "AUX"
	if cs_tag == "ANEGJUS":
		out_tag = "AUX"
	if cs_tag == "ANEGOPT":
		out_tag = "AUX"
	if cs_tag == "ANEGPST":
		out_tag = "AUX"
	if cs_tag == "ANY":
		out_tag = "AUX"
	if cs_tag == "AOPT":
		out_tag = "AUX"
	if cs_tag == "AOPT_PPERS":
		out_tag = "PRON"
	if cs_tag == "APREC":
		out_tag = "SCONJ"
	if cs_tag == "APST":
		out_tag = "AUX"
	if cs_tag == "ART":
		out_tag = "DET"
	if cs_tag == "CCIRC":
		out_tag = "SCONJ"
	if cs_tag == "CCOND":
		out_tag = "SCONJ"
	if cs_tag == "CFOC":
		out_tag = "PART"
	if cs_tag == "CONJ":
		out_tag = "CONJ"
	if cs_tag == "COP":
		out_tag = "PART"
	if cs_tag == "CPRET":
		out_tag = "AUX"
	if cs_tag == "CREL":
		out_tag = "SCONJ"
	if cs_tag == "EXIST":
		out_tag = "VERB"
	if cs_tag == "FM":
		out_tag = "X"
	if cs_tag == "FUT":
		out_tag = "AUX"
	if cs_tag == "IMOD":
		out_tag = "ADV"
	if cs_tag == "N":
		out_tag = "NOUN"
	if cs_tag == "NEG":
		out_tag = "ADV"
	if cs_tag == "NOUN":
		out_tag = "NOUN"
	if cs_tag == "NPROP":
		out_tag = "PROPN"
	if cs_tag == "NUM":
		out_tag = "NUM"
	if cs_tag == "PDEM":
		out_tag = "DET"
	if cs_tag == "PINT":
		out_tag = "PRON"
	if cs_tag == "PPERI":
		out_tag = "PRON"
	if cs_tag == "PPERO":
		out_tag = "PRON"
	if cs_tag == "PPERS":
		out_tag = "PRON"
	if cs_tag == "PPOS":
		out_tag = "DET"
	if cs_tag == "PREP":
		out_tag = "ADP"
	if cs_tag == "PTC":
		out_tag = "PART"
	if cs_tag == "PUNCT":
		out_tag = "PUNCT"
	if cs_tag == "UNKNOWN":
		out_tag = "X"
	if cs_tag == "V":
		out_tag = "VERB"
	if cs_tag == "VBD":
		out_tag = "VERB"
	if cs_tag == "VIMP":
		out_tag = "VERB"
	if cs_tag == "VSTAT":
		out_tag = "VERB"
	if out_tag == "":
		sys.stderr.write("unmapped: " + cs_tag +" on line " + str(line_num)+ "\n")
	return out_tag

infile = sys.argv[1]

lexfile = "C:\\treetagger\\bin\\coptic\\copt_lemma_lex.tab"

with open(lexfile) as lex:
	text = lex.read()

text = text.replace("\r","")
lemma_dict = defaultdict(lambda: defaultdict(str))
for line in text.split("\n"):
	if "\t" in line:
		row = line.split("\t")
		if not row[0].startswith("#"):
			lemma_dict[row[0]][row[1]] = row[2]

with open(infile) as corpus:
	text = corpus.read()

text = text.replace("\r","")
line_num = 0
for line in text.split("\n"):
	line_num += 1
	if "\t" in line:
		fields = line.split('\t')
		if fields[1] in lemma_dict:
			pass
#			if fields[3] in lemma_dict[fields[1]]:
#				fields[2] = lemma_dict[fields[1]][fields[3]]
#			else:
#				fields[2] = fields[1]
		else:
			fields[2] = fields[1]
		fields[4] = fields[3]
		fields[5] = "_"
		fields[3] = universalize(fields[3],line_num)
		print "\t".join(fields)
	else:
		print line