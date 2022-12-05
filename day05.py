from util import load_txt

col1 = ["Z", "J", "G"]
col2 = ["Q", "L", "R", "P", "W", "F", "V", "C"]
col3 = ["F", "P", "M", "C", "L", "G", "R"]
col4 = ["L", "F", "B", "W", "P", "H", "M"]
col5 = ["G", "C", "F", "S", "V", "Q"]
col6 = ["W", "H", "J", "Z", "M", "Q", "T", "L"]
col7 = ["H", "F", "S", "B", "V"]
col8 = ["F", "J", "Z", "S"]
col9 = ["M", "C", "D", "P", "F", "H", "B", "T"]

table = [col1, col2, col3, col4, col5, col6, col7, col8, col9]


def load():
    src = load_txt("day05.txt")
    raws = [y.replace(" ", "") for y in [x.replace("\n", "") for x in src]]
    raws = [x.split("from") for x in raws]
    return [
        [int(x.replace("move", "")), [int(z) for z in y.split("to")]] for [x, y] in raws
    ]


def move1(repeat: int, _from: int, _to: int):
    for _ in range(repeat):
        if table[_from - 1]:
            e = table[_from - 1].pop()
            table[_to - 1].append(e)


def solution1():
    data = load()
    [move1(x, y, z) for [x, [y, z]] in data]
    res = [x.pop() for x in table]
    return "".join(res)


def move2(repeat: int, _from: int, _to: int):
    moved = []
    for _ in range(repeat):
        if table[_from - 1]:
            e = table[_from - 1].pop()
            moved.insert(0, e)
    table[_to - 1] = [*table[_to - 1], *moved]


def solution2():
    data = load()
    [move2(x, y, z) for [x, [y, z]] in data]
    res = [x.pop() if x else " " for x in table]
    return "".join(res)


# print(solution1())

print(solution2())
