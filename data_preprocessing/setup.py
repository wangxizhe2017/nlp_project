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

# 介词
preposition = {
    "TO": "PRE",
    "IN": "CC", # of for from to at so with as
}

# 代词
pronoun = {
    "PRP": "PRP",
    "PRP$": "PRP",
    "WP": "PRP",
    "WP$": "PRP",
}

# 连词
conj = {
    "CC": "CC", # and but both
}

# 冠词
article = {
    "DT": "DT", # a an the no
    "WDT": "DT", # 定于从句提示词 which that
}

# 语助词
particle = {
    "UH": "UH",
    "INTJ": "UH",
}

# 标点
punctuation = {
    ",": "PUNC",
    ".": "PUNC",
    ":": "PUNC",
    "$": "PUNC",
    "''": "PUNC",
    "HYPH": "PUNC",
}

# 特殊
special = {
    "FW": "SPEC",
    "SYM": "SPEC",
    "CD": "NUM",
    "QP": "NUM", # 数字短语
    "POS": "POS", # 's
    "RP": "PART", # up
    "PRT": "PART", # up
}

unknown = {
    "UCP": "",  # 并列比较短语
    "CONJP": "",  # 连词短语
    "PP": "",  # 条件状语
    "SINV": "",  # ?
    "WHPP": "",  # 地点、时间、方式状语
    "SQ": "",  # 疑问
    "EX": "",  # there
    "SBAR": "",  # 从句
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
    "RP": "UP",
    "PRT": "UP",

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
    "S": "UNK",
}


if __name__ == "__main__":
    # print(len(noun) + len(verb) + len(adj) + len(adv) + len(preposition) + len(pronoun) + len(conj) + len(article) + len(particle)
    #       + len(punctuation) + len(special) + len(unknown))
    print(len(ALL_POS_TAGGER_DICT))


