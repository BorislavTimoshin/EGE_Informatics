from re import findall

with open("24_10724.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:[\dABCDEF]+)+", text)
    print(max(map(lambda x: x.lstrip("0"), sequences), key=len))
    print(len(max(map(lambda x: x.lstrip("0"), sequences), key=len)))
