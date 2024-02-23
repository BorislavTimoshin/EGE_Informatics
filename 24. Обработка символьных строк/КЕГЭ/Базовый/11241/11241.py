from re import findall

with open("24_11241.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:[^ABCD]+)+", text)
    print(max(sequences, key=len))
    print(len(max(sequences, key=len)))

# Или

maxim = 0
counter = 0
for i in range(len(text)):
    if text[i] not in "ABCD":
        counter += 1
        maxim = max(maxim, counter)
    else:
        counter = 0
print(maxim)
