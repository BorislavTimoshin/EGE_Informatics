from re import findall

with open("24_7723.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:[18][18][DR])+", text)
    print(sequences)
    print(len(max(sequences, key=len)) // 3)

