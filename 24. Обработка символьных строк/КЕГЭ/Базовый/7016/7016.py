from re import findall

with open("24_7016.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences1 = findall(r"A[^AD]+D", text)
    sequences2 = findall(r"D[^AD]+A", text)
    sequences = sequences1 + sequences2
    print(len(max(sequences, key=len)))
