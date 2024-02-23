from re import findall

with open("24_5171.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:CA)+", text)
    h = max(sequences, key=len)
    print(len(h), h)
