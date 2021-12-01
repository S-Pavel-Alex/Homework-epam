"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
import string


def get_longest_diverse_words(file_path: str) -> List[str]:
    my_dict = {}
    with open(file_path, encoding='raw_unicode_escape') as fi:
        line_all = fi.read()
        line_all = line_all.split()
        for element in line_all:
            if element not in my_dict:
                my_dict[element] = 0
        new_line = sorted(my_dict, key=len, reverse=True)
        final_li = new_line[:10]
        return final_li


def get_rarest_char(file_path: str) -> str:
    my_dir = {}
    dir_all = {}
    with open(file_path, encoding='raw_unicode_escape') as fi:
        for line in fi:
            for element in line:
                if element in my_dir:
                    my_dir[element] += 1
                else:
                    my_dir[element] = 1
        for k, v in my_dir.items():
            dir_all[v] = k
        return dir_all[min(dir_all)]


def count_punctuation_chars(file_path: str) -> int:
    total = 0
    with open(file_path) as fi:
        for line in fi:
            for element in line:
                if element in string.punctuation:
                    total += 1
    return total


def count_non_ascii_chars(file_path: str) -> int:
    my_list = []
    with open(file_path, encoding='raw_unicode_escape') as fi:
        for line in fi:
            for element in line:
                if not element.isascii():
                    my_list.append(element)
    return len(my_list)


def get_most_common_non_ascii_char(file_path: str) -> str:
    my_dir = {}
    dir_all = {}
    with open(file_path, encoding='raw_unicode_escape') as fi:
        line_all = fi.read()
        line = line_all.split()
        for element in line:
            if not element.isascii():
                if element in my_dir:
                    my_dir[element] += 1
                else:
                    my_dir[element] = 1
        for k, v in my_dir.items():
            dir_all[v] = k
        key_max = max(dir_all.keys())
    return dir_all[key_max]
