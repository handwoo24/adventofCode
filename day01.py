from typing import List


def slice_at_empty(values: List[str]) -> List[int]:
    def _slice(_list: List[str]):
        group = []
        for l in _list:
            if l == "":
                yield group
                group = []
            else:
                group.append(int(l))

    return list(_slice(values))


def load_inputs():
    src = "day01.txt"

    with open(src, "r") as s:
        lines = s.readlines()

    data = [l.replace("\n", "") for l in lines]

    return slice_at_empty(data)


def solution1() -> int:
    inputs = load_inputs()
    return max([sum(i) for i in inputs])


def solution2() -> int:
    inputs = load_inputs()
    return sum(sorted([sum(i) for i in inputs], reverse=True)[:3])


answer1 = solution1()

answer2 = solution2()

print(answer1, answer2)
