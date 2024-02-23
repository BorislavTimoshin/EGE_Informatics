from re import findall


with open("24_2420.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"[ABEF]+", text)
    print(max(sequences, key=len))
    print(len(max(sequences, key=len)))
