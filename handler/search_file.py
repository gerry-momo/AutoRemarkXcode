# coding=utf-8
import os


def find_file(path, all_file):
    path_list = os.listdir(path)
    for new_path in path_list:
        new_path = os.path.join(path, new_path)

        if os.path.isdir(new_path):
            find_file(new_path, all_file)
        elif os.path.isfile(new_path):
            suffix_name = os.path.splitext(new_path)[1]

            if suffix_name in [".swift"]:  # 指定文件后缀名
                all_file.append(new_path)
