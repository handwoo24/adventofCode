from typing import List
from util import load_txt


inputs = [t.replace("\n", "").split(" ") for t in load_txt("day02.txt")]

opponents = ["A", "B", "C"]

mines = ["X", "Y", "Z"]


def scored1(x: str, y: str) -> int:
    index_y = mines.index(y)
    if x == opponents[index_y - 1]:
        return 6 + index_y + 1
    elif x == opponents[index_y]:
        return 3 + index_y + 1
    else:
        return 0 + index_y + 1


def rounds1(values: List[str]) -> List[int]:
    [x, y] = values
    return scored1(x, y)


def solution1():
    return sum([rounds1(i) for i in inputs])


def scored2(x: str, y: str) -> int:
    index_x = opponents.index(x)
    index_y = mines.index(y)
    trims = [-1, 0, -2]
    yy = mines[index_x + trims[index_y]]
    index_yy = mines.index(yy)
    scores = [0, 3, 6]
    return scores[index_y] + index_yy + 1


def rounds2(values: List[str]) -> List[int]:
    [x, y] = values
    return scored2(x, y)


def solution2():
    return sum([rounds2(i) for i in inputs])


print(solution1())

print(solution2())
