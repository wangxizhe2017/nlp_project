from data_preprocessing.file_process import *


def parse_sentence(sentence_str):
    pass


if __name__ == "__main__":
    file_path_name_list = get_file_path_name_list_in_path(PARSED_DATA_PATH)

    print(file_path_name_list)

    get_string_list_line_by_line_from_test(file_path_name_list[0])

