def load_txt(path: str):
    with open(path, "r") as s:
        return s.readlines()
