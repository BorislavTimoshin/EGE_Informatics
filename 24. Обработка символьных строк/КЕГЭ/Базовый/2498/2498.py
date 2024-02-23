from re import findall

with open("24_2498.txt", "r", encoding="utf-8") as file:
    text = file.read()

counter = 0
for i in range(len(text)):
    s = text[i:i+3]
    if s == "XIX":
        counter += 1
print(counter)
