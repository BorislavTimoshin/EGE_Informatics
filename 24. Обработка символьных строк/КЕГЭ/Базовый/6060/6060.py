with open("24_6060.txt", "r", encoding="utf-8") as file:
    text = file.read()
    counter = 0
    for i in range(len(text)):
        word = text[i:i+9]
        if word == word[::-1]:
            counter += 1

print(counter)
