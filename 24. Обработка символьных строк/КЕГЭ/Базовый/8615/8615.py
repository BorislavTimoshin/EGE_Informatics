from re import fullmatch

with open("24_8615.txt", "r", encoding="utf-8") as file:
    text = file.read()

counter = 2
maxim = 0
for i in range(len(text) - 2):
    s1, s2, s3 = text[i], text[i+1], text[i+2]
    s = s1 + s2 + s3
    if fullmatch(r'[A-F]{3}', s):
        counter = 2
    else:
        counter += 1
        maxim = max(maxim, counter)
print(maxim)
