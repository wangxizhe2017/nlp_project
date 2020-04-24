import os
import csv
from tqdm import tqdm
from data_preprocessing.log_writer import *


if __name__ == "__main__":
    with open("C:\\Users\\caesar\\Desktop\\1\\train_combined.csv", encoding='utf_8', newline='') as csv_file:
        f = csv.reader(csv_file)
        for i, line in enumerate(tqdm(list(f), ncols=80, leave=False)):
            if 0 < i:
                print("{:5d}: {}".format(i, line[5]))
                s = line[5].replace("\"", "'").replace("���", "'").replace("��", "'").replace("�", "'")
                write_string("{\"sentence\": \"%s\"}" % (s), file_name="train_sentence_5.json", path="C:\\Users\\caesar\\Desktop\\1\\")

