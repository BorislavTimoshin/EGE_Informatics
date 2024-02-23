with open("24_4546.txt", "r", encoding="utf-8") as file:
    text = file.read()
    counter = 0
    maxim = 0
    for j in range(3):
        for i in range(j, len(text) - 2, 3):
            if text[i] == text[i+2] == "A" or text[i] == text[i + 2] == "C":
                counter += 1
                maxim = max(maxim, counter)
            else:
                counter = 0
        counter = 0
    print(maxim)
