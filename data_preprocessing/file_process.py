from os import listdir
from os.path import isfile, join


ROOT_PATH = "./"
PARSED_DATA_PATH = join(ROOT_PATH, "parsed_data")
REORGANIZED_DATA_PATH = join(ROOT_PATH, "reorganized_data")


def get_file_name_list_in_path(path_name):
    return [file_name for file_name in listdir(path_name) if isfile(join(path_name, file_name))]


def get_file_path_name_list_in_path(path_name):
    file_name_list = get_file_name_list_in_path(path_name)

    file_path_name_list = []
    for file_name in file_name_list:
        file_path_name_list.append(join(path_name, file_name))

    return file_path_name_list


def get_string_list_line_by_line_from_test(test_file_path_name):
    string_list = []
    with open(test_file_path_name, "r") as test_file:
        for i, line in enumerate(test_file):
            string_list.append(line)
            # print("line_{:4d}: {}".format(i+1, line))

    return string_list

