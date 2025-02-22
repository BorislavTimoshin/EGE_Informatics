from re import findall

with open("24_8166.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"[ABC]+", text)
    print(len(max(sequences, key=len)) // 2)

