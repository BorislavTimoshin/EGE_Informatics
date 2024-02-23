from re import findall

with open("24_4021.txt", "r", encoding="utf-8") as file:
    text = file.read()
    # sequences = findall(r"(?:BB|DD)+", text)
    # print(len(max(sequences, key=len)) // 2 + 1)  # Необходимо проверить в файле

# Или
words = text.split(".")
maxim = 0
max_d = []
for i in range(len(words) - 5):
    d = words[i:i+6]
    if len("".join(d)) > maxim:
        max_d = d
    maxim = max(maxim, len("".join(d)))
print(maxim + 5)

