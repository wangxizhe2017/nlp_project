import os
import csv
import pandas as pd
from tqdm import tqdm
import random as rd
from data_preprocessing.log_writer import *


def get_sentence_from_scv(csv_file_name, csv_path, sentence_num, json_file_prefix, json_path="./json_sentence", opt=0):
    print("{}, sentence_num={}, opt={}".format(csv_file_name, sentence_num, opt))
    with open(os.path.join(csv_path, csv_file_name), encoding='utf_8', newline='') as csv_file:
        f = csv.reader(csv_file)
        for i, line in enumerate(tqdm(list(f), ncols=80, leave=False)):
            if 0 < i:
                print("{:5d}: {}".format(i, line[sentence_num + (0 if opt == 0 else opt - 1)]))
                s = line[sentence_num + (0 if opt == 0 else opt - 1)].replace("\"", "'").replace("\\", "").replace("���", "'").replace("��", "'").replace("�", "'")

                file_name = "{}_sentence_{}".format(json_file_prefix, sentence_num)
                file_name += "_opt{}.json".format(opt) if opt > 0 else ".json"
                write_string("{\"sentence\": \"%s\"}" % (s), file_name=file_name, path=json_path)


def random_swap_two_columns_in_csv(file_name, path, swap_1, swap_2, label):
    df = pd.read_csv(os.path.join(path, file_name), index_col=0)

    for i, (sentence1, sentence2) in enumerate(zip(df[swap_1], df[swap_2])):
        if i >= 0:
            print("{}; {}".format(sentence1, sentence2))
            print("{}; {}".format(df[swap_1][i], df[swap_2][i]))
            if rd.randint(1, 2) == 2:
                df[swap_1][i] = sentence2
                df[swap_2][i] = sentence1
                df[label][i] = 2

            else:
                df[label][i] = 1

    df.to_csv(os.path.join(path, file_name))


if __name__ == "__main__":
    # testing data
    get_sentence_from_scv("cloze_test_test__spring2016 - cloze_test_ALL_test.csv", "../data", 1, json_file_prefix="test")
    get_sentence_from_scv("cloze_test_test__spring2016 - cloze_test_ALL_test.csv", "../data", 2, json_file_prefix="test")
    get_sentence_from_scv("cloze_test_test__spring2016 - cloze_test_ALL_test.csv", "../data", 3, json_file_prefix="test")
    get_sentence_from_scv("cloze_test_test__spring2016 - cloze_test_ALL_test.csv", "../data", 4, json_file_prefix="test")
    get_sentence_from_scv("cloze_test_test__spring2016 - cloze_test_ALL_test.csv", "../data", 5, json_file_prefix="test", opt=1)
    get_sentence_from_scv("cloze_test_test__spring2016 - cloze_test_ALL_test.csv", "../data", 5, json_file_prefix="test", opt=2)
    # validation data
    get_sentence_from_scv("spring_winter_combined.csv", "../data", 1, json_file_prefix="val")
    get_sentence_from_scv("spring_winter_combined.csv", "../data", 2, json_file_prefix="val")
    get_sentence_from_scv("spring_winter_combined.csv", "../data", 3, json_file_prefix="val")
    get_sentence_from_scv("spring_winter_combined.csv", "../data", 4, json_file_prefix="val")
    get_sentence_from_scv("spring_winter_combined.csv", "../data", 5, json_file_prefix="val", opt=1)
    get_sentence_from_scv("spring_winter_combined.csv", "../data", 5, json_file_prefix="val", opt=2)
    # training data
    # get_sentence_from_scv("train_combined.csv", "../data", 5, json_file_prefix="train")

    # random_swap_two_columns_in_csv("my_test.csv", "C:\\Users\\caesar\\Desktop\\1\\", "a1", "b2", "AnswerRightEnding")

