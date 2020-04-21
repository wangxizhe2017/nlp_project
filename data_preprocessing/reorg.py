from data_preprocessing.file_process import *
from data_preprocessing.setup import *


# The first job is to find all the part-of-speech (pos) taggers occurred in data-set
def parse_pos_tagger_from_line(line):
    pos_tagger_set = set({})

    tagger_started = False
    pos_tagger = ""
    for c in line:
        if c == "(":
            tagger_started = True
            continue

        if tagger_started:
            if c == " ":
                pos_tagger_set.add(pos_tagger)
                tagger_started = False
                pos_tagger = ""

            else:
                pos_tagger += c

    return pos_tagger_set


def get_all_pos_tagger_from_data_set(path_name):
    pos_tagger_set = set({})

    file_path_name_list = get_file_path_name_list_in_path(path_name)

    for file_path_name in file_path_name_list:
        line_list = get_string_list_line_by_line_from_test(file_path_name)

        for line in line_list:
            pos_tagger_set = set.union(pos_tagger_set, parse_pos_tagger_from_line(line))

    print(len(pos_tagger_set))
    print(pos_tagger_set)
    return pos_tagger_set
# end of first job: find all the part-of-speech (pos) taggers occurred in data-set


def parse_sentence(sentence_str):
    pass


if __name__ == "__main__":
    get_all_pos_tagger_from_data_set(PARSED_DATA_PATH)

