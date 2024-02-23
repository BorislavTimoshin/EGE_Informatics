from re import findall

with open("24_4643.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:[12]{2}[AB])+", text)
    h = max(sequences, key=len)
    print(len(h) // 3, h)
