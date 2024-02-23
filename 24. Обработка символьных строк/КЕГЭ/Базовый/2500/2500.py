from re import findall

with open("24_2500.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"G.ME", text)
    print(len(sequences))
