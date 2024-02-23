from re import findall

with open("24_9850.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:[^LISENOK]+)+", text)
    print(len(max(sequences, key=len)))
