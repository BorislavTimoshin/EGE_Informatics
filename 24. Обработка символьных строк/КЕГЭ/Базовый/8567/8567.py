from re import search

with open("24_8567.txt", "r", encoding="utf-8") as file:
    text = file.read()

counter = 0
s = ""
maxim = 0
for i in range(len(text)):
    if search(r'[A-D]{3}', s + text[i]):
        counter = 2
        s = s[-1] + text[i]
    else:
        counter += 1
        s += text[i]
        maxim = max(maxim, counter)
print(maxim)
