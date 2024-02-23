from re import findall


with open("24_2421.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"[^D]+", text)
    print(max(sequences, key=len))
    print(len(max(sequences, key=len)))
