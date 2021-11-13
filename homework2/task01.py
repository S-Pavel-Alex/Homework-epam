"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


# def get_longest_diverse_words(file_path: str) -> List[str]:
    # my_dict = {}
    # with open(file_path) as fi:


def get_rarest_char(file_path: str) -> str:
    my_dict = {}
    with open(file_path) as fi:
        for line in fi:
            for e in line:
                if e in my_dict:
                    my_dict[e] += 1
                else:
                    my_dict[e] = 1
    return max(my_dict)


def count_punctuation_chars(file_path: str) -> int:
    punctuation_chars = ['.', ',', '!', '?']
    all_char = []
    with open(file_path) as fi:
        for line in fi:
            for e in line:
                if e in punctuation_chars:
                    all_char.append(e)
    return len(all_char)


def count_non_ascii_chars(file_path: str) -> int:
    count = 0
    with open(file_path) as fi:
        for line in fi:
            for e in line:
                if not e.isascii():
                    count += 1
    return count


# def get_most_common_non_ascii_char(file_path: str) -> str:
    ...



print(get_rarest_char('data.txt'))
print(count_punctuation_chars('data.txt'))
print(count_non_ascii_chars('data2.txt'))
