from re import findall

with open("24_2425.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:DBAC)+", text)
    print(len(max(sequences, key=len)) + 3)
