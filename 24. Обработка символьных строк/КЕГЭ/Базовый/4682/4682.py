from re import findall

with open("24_4682.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:[AE][BCD])+", text)
    h = max(sequences, key=len)
    print(len(h) // 2, h)
