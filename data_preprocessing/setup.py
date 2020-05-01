ALL_POS_TAGGER_SET = {"WP$", "ADVP", "PP", "RBR", "X", ",", "VBG", "JJR", "UCP", "IN", "$", "VBN", "SINV", "PDT", "JJ", "XX", "NP", "WHPP", "MD",
                      "NNS", "CD", "WRB", "POS", "HYPH", "RBS", "SQ", "PRP$", "JJS", "VP", "CC", ".", "DT", "SYM", "WDT", "FW", "EX", "''", "SBAR",
                      ":", "TO", "PRN", "INTJ", "FRAG", "WHNP", "WHADJP", "NN", "WHADVP", "UH", "S", "PRT", "RP", "VBZ", "VB", "NNPS", "VBP", "QP",
                      "PRP", "SBARQ", "WP", "CONJP", "NNP", "VBD", "ADJP", "RB"}

noun = {
    "NN": "NN",
    "NP": "NN",
    "NNS": "NN",
    "NNP": "NN",
    "NNPS": "NN",
    "WHNP": "NN",
}

verb = {
    "MD": "VB", # will can would could
    "VB": "VB",
    "VP": "VB",
    "VBD": "VB",
    "VBP": "VB",
    "VBG": "VB",
    "VBN": "VB",
    "VBZ": "VB",
}

adj = {
    "JJ": "ADJ",
    "JJR": "ADJ",
    "JJS": "ADJ",
    "ADJP": "ADJ",
    "WHADJP": "ADJ",
    "PDT": "ADJ", # all quite
}

adv = {
    "RB": "ADV",
    "RBR": "ADV",
    "RBS": "ADV",
    "WRB": "ADV",
    "ADVP": "ADV",
    "WHADVP": "ADV",
}

preposition = {
    "TO": "PRE",
    "IN": "CC", # of for from to at so with as
}

pronoun = {
    "PRP": "PRP",
    "PRP$": "PRP",
    "WP": "PRP",
    "WP$": "PRP",
}

conj = {
    "CC": "CC", # and but both
}

article = {
    "DT": "DT", # a an the no
    "WDT": "DT", # which that
}

particle = {
    "UH": "UH",
    "INTJ": "UH",
}

punctuation = {
    ",": "PUNC",
    ".": "PUNC",
    ":": "PUNC",
    "$": "PUNC",
    "''": "PUNC",
    "HYPH": "PUNC",
}

special = {
    "FW": "SPEC",
    "SYM": "SPEC",
    "CD": "NUM",
    "QP": "NUM", #
    "POS": "POS", # 's
    "RP": "PART", # up
    "PRT": "PART", # up
}

unknown = {
    "UCP": "",
    "CONJP": "",
    "PP": "",
    "SINV": "",  # ?
    "WHPP": "",
    "SQ": "",
    "EX": "",  # there
    "SBAR": "",
    "PRN": "",
    "SBARQ": "",
    "FRAG": "",
    "X": "",
    "XX": "",
    "S": "",
}

# ========================================================================================================================

UPPER_POS_TAGGER_SET = {"N", "V", "ADJ", "ADV", "PRE", "PRP", "CC", "DT", "UH", "PUNC", "SPEC", "NUM", "POS", "UP", "UNK"}

ALL_POS_TAGGER_DICT = {
    "S": "S",

    "NN": "N",
    "NP": "N",
    "NNS": "N",
    "NNP": "N",
    "NNPS": "N",
    "WHNP": "N",

    "MD": "V",
    "VB": "V",
    "VP": "V",
    "VBD": "V",
    "VBP": "V",
    "VBG": "V",
    "VBN": "V",
    "VBZ": "V",

    "JJ": "ADJ",
    "JJR": "ADJ",
    "JJS": "ADJ",
    "ADJP": "ADJ",
    "WHADJP": "ADJ",
    "PDT": "ADJ",

    "RB": "ADV",
    "RBR": "ADV",
    "RBS": "ADV",
    "WRB": "ADV",
    "ADVP": "ADV",
    "WHADVP": "ADV",

    "TO": "PRE",
    "IN": "PRE",
    "RP": "UP",
    "PRT": "UP",

    "PRP": "PRP",
    "PRP$": "PRP",
    "WP": "PRP",
    "WP$": "PRP",

    "CC": "CC",

    "DT": "DT",
    "WDT": "DT",

    "UH": "UH",
    "INTJ": "UH",

    ",": "PUNC",
    ".": "PUNC",
    ":": "PUNC",
    "$": "PUNC",
    "''": "PUNC",
    "HYPH": "PUNC",

    "FW": "SPEC",
    "SYM": "SPEC",
    "CD": "NUM",
    "QP": "NUM",

    "POS": "POS",

    "UCP": "UNK",
    "CONJP": "UNK",
    "PP": "UNK",
    "SINV": "UNK",
    "WHPP": "UNK",
    "SQ": "UNK",
    "EX": "UNK",
    "SBAR": "UNK",
    "PRN": "UNK",
    "SBARQ": "UNK",
    "FRAG": "UNK",
    "X": "UNK",
    "XX": "UNK",
}


MUST_KEEP_WORD_SET = {"no", "not", "n't", "yes", "all", "both", "or"}
KEEP_SET = {"NN", "NP", "NNS", "NNP", "NNPS", "WHNP", "MD", "VB", "VP", "VBD", "VBP", "VBG", "VBN", "VBZ",
            "JJ", "JJR", "JJS", "ADJP", "WHADJP", "PDT", "RB", "RBR", "RBS", "WRB", "ADVP", "WHADVP",
            "CC", "CD", "EX", "SYM", "QP", "RP", "PRT", "FW", "SYM",
            ",", ".", ":", "''"}


VERB_ADJ_ADV_DICT = {
    "MD": "V",
    "VB": "V",
    "VP": "V",
    "VBD": "V",
    "VBP": "V",
    "VBG": "V",
    "VBN": "V",
    "VBZ": "V",

    "JJ": "ADJ",
    "JJR": "ADJ",
    "JJS": "ADJ",
    "ADJP": "ADJ",
    "WHADJP": "ADJ",
    "PDT": "ADJ",

    "RB": "ADV",
    "RBR": "ADV",
    "RBS": "ADV",
    "WRB": "ADV",
    "ADVP": "ADV",
    "WHADVP": "ADV",
}


GET_SENTENCE_FROM_SCV = True
GENERATE_REORGANIZE_SENTENCE = False
SWAP_OPTION1_AND_OPTION2 = False


if __name__ == "__main__":
    # print(len(noun) + len(verb) + len(adj) + len(adv) + len(preposition) + len(pronoun) + len(conj) + len(article) + len(particle)
    #       + len(punctuation) + len(special) + len(unknown))
    print(len(ALL_POS_TAGGER_DICT))


