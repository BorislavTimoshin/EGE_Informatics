from re import findall

with open("24_4642.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:[AB][12])+", text)
    h = max(sequences, key=len)
    print(len(h) // 2, h)
