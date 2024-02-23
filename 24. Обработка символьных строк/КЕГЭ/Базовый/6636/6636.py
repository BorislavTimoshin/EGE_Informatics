from re import findall

with open("24_6636.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:[24][135])+", text)
    print(len(max(sequences, key=len)) // 2)
