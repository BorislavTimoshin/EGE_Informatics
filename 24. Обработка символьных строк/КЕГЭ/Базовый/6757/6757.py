from re import findall

with open("24_6757.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:CFE|FCE)+", text)
    print(len(max(sequences, key=len)) // 3)
