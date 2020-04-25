import spacy
from nltk.corpus import wordnet as wn

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

    file_path_name_list = get_file_path_name_list_in_dir(path_name)

    for file_path_name in file_path_name_list:
        line_list = get_string_list_line_by_line_from_text(file_path_name)

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
            return True, post_list[l - i]

    return False


def parse_sentence(sentence_str):
    word_keep_list = []
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
                    word_keep_list.append(word)
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
    for i, word in enumerate(word_keep_list):
        if i == 0:
            sentence += word

        elif i == len(word_keep_list) - 1:
            sentence += word

        else:
            sentence += " " + word

    # print("keep: {}".format(word_keep_list))
    # print("remo: {}".format(word_remove))

    return sentence


# ====================================================================================================


def recursive_post(all_post_list, limit_num):
    l = len(all_post_list) - 1

    curr_post = ""
    for i in range(limit_num):
        if all_post_list[l - i] == "":
            break

        else:
            curr_post = VERB_ADJ_ADV_DICT[all_post_list[l - i]] if all_post_list[l - i] in VERB_ADJ_ADV_DICT else "OTHER"

    return curr_post


def sentence_and_post(sentence_str):
    word_list = []
    post_list = []
    all_post_list = []

    word = ""
    post = ""
    focus_word = False
    focus_post = False
    right_bracket_num = 0
    for c in sentence_str.replace("\"", ""):
        if c == "(":
            post = ""
            focus_post = True
            focus_word = False

        elif c == ")":
            right_bracket_num += 1

        elif c == " " or c == "\n":
            if focus_post:
                all_post_list.append(post)

                word = ""
                focus_post = False
                focus_word = True

            elif focus_word:
                word_list.append(word)
                post_list.append(recursive_post(all_post_list, right_bracket_num))
                all_post_list[-1] = ""

                focus_post = False
                focus_word = False
                right_bracket_num = 0

        elif focus_post:
            post += c

        elif focus_word:
            word += c

    # print(word_list)
    # print(post_list)
    # print(all_post_list)

    return word_list, post_list


def parse_and_reorganize_sentence(path):
    file_name_list = get_file_name_list_in_dir(path)

    for i, file_name in enumerate(file_name_list):
        line_list = get_string_list_line_by_line_from_text(join(path, file_name))

        for j, line in enumerate(line_list):
            reorganized_sentence = parse_sentence(line)
            write_string(reorganized_sentence, file_name=file_name, path="reorganized_data")


def generate_sentence_and_post(path):
    file_name_list = get_file_name_list_in_dir(path)

    for i, file_name in enumerate(file_name_list):
        if file_name != "train_sentence_5.txt":
            continue

        line_list = get_string_list_line_by_line_from_text(join(path, file_name))

        for j, line in enumerate(line_list):
            word_list, post_list = sentence_and_post(line)
            write_string(str("{}\t{}".format(word_list, post_list)), file_name=file_name, path="antonym_sentence")


def get_antonyms(word):
    antonyms = []
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            if l.antonyms():
                antonyms.append(l.antonyms()[0].name())
    if len(antonyms) > 0:
        return antonyms[0]


def antonym_generator_main(line):
    line = line.split('\t')
    left = line[0][2:-3].split("', '")
    right = line[1][2:-3].split("', '")
    zipped = zip(left, right)
    new_line = list()
    count = 0
    for i, word in enumerate(zipped):
        # if word[0] == "n\'t":
        #     del left[i]
        #     new_line.append(left)
        #     break
        if word[1] == 'ADJ' or word[1] == 'ADV' and get_antonyms(word[0]):
            count += 1
            if count % 2 == 1:
                new_line.append(get_antonyms(word[0]))
            else:
                new_line.append(word[0])
        elif word[1] == 'V':
            count += 1
            if count % 2 == 1:
                new_line.append('not')
                new_line.append(word[0])
            else:
                new_line.append(word[0])
        else:
            new_line.append(word[0])

    sentence = ""
    for i, word in enumerate(new_line):
        if word is None:
            continue

        if i == 0:
            sentence += word

        elif i == len(new_line) - 1:
            sentence += word

        elif word.find("\'") != -1:
            sentence += word

        elif word == ",":
            sentence += word

        else:
            sentence += " " + word

    return sentence


def generate_whole_train_csv(path):
    file_name_list = get_file_name_list_in_dir(path)

    for i, file_name in enumerate(file_name_list):
        line_list = get_string_list_line_by_line_from_text(join(path, file_name))
        for j, line in enumerate(line_list):
            antonym_sentence = antonym_generator_main(line)
            write_string(antonym_sentence, file_name="train_sentence_5_antonym.txt", path=path)


if __name__ == "__main__":
    # get_all_pos_tagger_from_data_set(PARSED_DATA_PATH)

    # parse_and_reorganize_sentence(PARSED_DATA_PATH)
    # generate_sentence_and_post(PARSED_DATA_PATH)
    generate_whole_train_csv(ANTONYM_PATH)

