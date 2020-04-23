import os
import datetime

Path_STD = "./reorganized_data/"
Log_Name = "log.txt"


def write_string(str_to_write, file_name=Log_Name, path=Path_STD, end=None):
    file_path_name = os.path.join(path, file_name)

    file = open(file_path_name, 'a+')
    file.write("{}{}".format(str_to_write, end if end is not None else "\n"))
    print(str_to_write, end=end)
    file.close()


if __name__ == "__main__":
    print("log_writer.py")

    s = "try"
    end = ":"
    file = open("ttt.txt", "a+")
    file.write("{}{} {}".format(s, end, ""))
    print("{}{} ".format(s, end))
    # print("\"%s\" is written to %s\n" % (str_to_write, file_path_name))
    file.close()
