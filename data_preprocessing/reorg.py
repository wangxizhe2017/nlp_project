import spacy

from data_preprocessing.file_process import *
from data_preprocessing.setup import *
from data_preprocessing.log_writer import *


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


def keep_word(post_list, limit_num):
    l = len(post_list) - 1

    for i in range(limit_num):
        if post_list[l - i] == "":
            break

        if post_list[l - i] in KEEP_SET:
            return True

    return False


def parse_sentence(sentence_str):
    word_keep = []
    word_remove = []

    level = 0
    right_bracket_num = 0
    post = ""
    word = ""
    post_list = []
    focus_post = False
    focus_word = False
    for c in sentence_str.replace("\"", ""):
        if c == "(":
            post = ""
            focus_post = True
            focus_word = False

        elif c == ")":
            right_bracket_num += 1

        elif c == " " or c == "\n":
            if focus_post:
                post_list.append(post)

                focus_post = False
                focus_word = True

            elif focus_word:
                if keep_word(post_list, right_bracket_num):
                    word_keep.append(word)
                    post_list[-1] = ""

                else:
                    word_remove.append(word)

                focus_post = False
                focus_word = False
                right_bracket_num = 0

            # post = "" # no need to do it here
            word = ""

        elif focus_post:
            post += c

        elif focus_word:
            word += c

    sentence = ""
    for i, word in enumerate(word_keep):
        if i == 0:
            sentence += word

        elif i == len(word_keep) - 1:
            sentence += word

        else:
            sentence += " " + word

    # print("keep: {}".format(word_keep))
    # print("remo: {}".format(word_remove))

    return sentence


if __name__ == "__main__":
    # get_all_pos_tagger_from_data_set(PARSED_DATA_PATH)

    file_name_list = get_file_name_list_in_dir(PARSED_DATA_PATH)

    for i, file_name in enumerate(file_name_list):
        line_list = get_string_list_line_by_line_from_text(join(PARSED_DATA_PATH, file_name))

        for j, line in enumerate(line_list):
            reorganized_sentence = parse_sentence(line)
            write_string(reorganized_sentence, file_name=file_name)

