from re import findall

with open("24_6054.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:[BC]{2}A)+", text)
    print(len(max(sequences, key=len)))
