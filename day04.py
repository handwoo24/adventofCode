from util import load_txt


data = [x.replace("\n", "") for x in load_txt("day04.txt")]


def check1(raw: str):
    [elf1, elf2] = raw.split(",")
    [s1, e1] = elf1.split("-")
    [s2, e2] = elf2.split("-")
    set1 = set(range(int(s1), int(e1) + 1))
    set2 = set(range(int(s2), int(e2) + 1))
    if set1.issubset(set2):
        return True
    elif set2.issubset(set1):
        return True
    else:
        return False


def check2(raw: str):
    [elf1, elf2] = raw.split(",")
    [s1, e1] = elf1.split("-")
    [s2, e2] = elf2.split("-")
    set1 = set(range(int(s1), int(e1) + 1))
    set2 = set(range(int(s2), int(e2) + 1))
    if set1.intersection(set2):
        return True
    else:
        return False


def solution1():
    return [check1(x) for x in data].count(True)


def solution2():
    return [check2(x) for x in data].count(True)


print(solution1())

print(solution2())
