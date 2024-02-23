from re import findall

with open("24_12254.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:RSQ)+", text)
    print(max(sequences, key=len))
    print(len("RSQRSQRSQRSQRSQRSQRSQRSQRSQRSQRSQRSQRSQRSQRSQRSQRSQ") + 3)
