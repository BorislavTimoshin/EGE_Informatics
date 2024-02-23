from re import findall

with open("24_3021.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:ZXY|ZYX)+", text)
    print(len(max(sequences, key=len)) // 3)


counter = 0
maxim = 0
for j in range(2):
    for i in range(j, len(text) - 2, 3):
        s = text[i:i+3]
        if s == "ZXY" or s == "ZYX":
            counter += 1
            maxim = max(maxim, counter)
        else:
            counter = 0
    counter = 0
print(maxim)
