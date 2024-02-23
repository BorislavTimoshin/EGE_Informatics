with open("24_2531.txt", "r", encoding="utf-8") as file:
    text = file.read()

counter = 0
for i in range(len(text)):
    s = text[i:i+7]
    if s == "NEWYEAR":
        counter += 1
print(counter)
