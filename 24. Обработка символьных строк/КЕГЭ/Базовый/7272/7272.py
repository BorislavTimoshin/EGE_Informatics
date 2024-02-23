from re import findall

with open("24_7272.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:AB|CB)+", text)
    print(len(max(sequences, key=len)) // 2)


