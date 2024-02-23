with open("24_2497.txt", "r", encoding="utf-8") as file:
    text = file.read()

counter = 0
for i in range(len(text)):
    s = text[i:i+5]
    if s == "XVIII":
        counter += 1
print(counter)
