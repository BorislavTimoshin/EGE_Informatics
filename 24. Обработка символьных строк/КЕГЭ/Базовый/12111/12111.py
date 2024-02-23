from re import findall

with open("24_12111.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:NYN|HPY)+", text)
    print(max(sequences, key=len))
print(len("NYNHPYNYNNYNNYNHPYNYNNYNHPYHPYHPYNYNHPYNYNNYNHPY") // 3)

# Или

counter = 0
maxim = 0
for j in range(3):
    for i in range(j, len(text) - 2, 3):
        if text[i:i+3] == "NYN" or text[i:i+3] == "HPY":
            counter += 1
            maxim = max(counter, maxim)
        else:
            counter = 0
    counter = 0
print(maxim)
