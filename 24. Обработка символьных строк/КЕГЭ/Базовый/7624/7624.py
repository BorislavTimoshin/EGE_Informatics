from re import findall
from re import search

with open("24_7624.txt", "r", encoding="utf-8") as file:
    text = file.read()
    # sequences = findall(r"(?:[18][18][DR])+", text)

counter = 0
maxim = 0
s = ""
for i in range(len(text)):
    if search(r'[XYZ]{2}', s + text[i]):
        counter = 1
        s = text[i]
    else:
        counter += 1
        s += text[i]
        maxim = max(maxim, counter)
print(maxim)
