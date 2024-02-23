from re import findall

with open("24_6029.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences1 = findall(r"(?:EF)+", text)
    sequences2 = findall(r"(?:FE)+", text)
    sequences = sequences1 + sequences2
    print(len(max(sequences, key=len)) + 1)
