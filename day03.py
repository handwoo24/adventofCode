from typing import List
from math import floor, ceil
from util import load_txt
from string import ascii_letters


data = [x.replace("\n", "") for x in load_txt("day03.txt")]


def split(raw: str) -> List[str]:
    half = floor(len(raw) / 2)
    return [raw[:half], raw[half:]]


def get_share_char(comp1: str, comp2: str) -> int:
    for x in comp2:
        if x in comp1:
            return ascii_letters.index(x) + 1


def solution1():
    splited = [split(x) for x in data]
    numx = [get_share_char(x, y) for [x, y] in splited]
    return sum(numx)


def split_by3(data: List[str]):
    length = len(data)
    q = ceil(length / 3)
    res = []
    for i in range(q):
        res.append(data[i * 3 : (i + 1) * 3])
    return res


def get_group_badge(group: List[str]):
    head = group[0]
    for char in head:
        checks = [char in x for x in group]
        if len([x for x in checks if x]) == 3:
            return ascii_letters.index(char) + 1


def solution2():
    splited = split_by3(data)
    return sum([get_group_badge(x) for x in splited])


def test2():
    test_data = [x.replace("\n", "") for x in load_txt("test03.txt")]
    splited = split_by3(test_data)
    return sum([get_group_badge(x) for x in splited])


print(solution1())

print(solution2())

print(test2())
