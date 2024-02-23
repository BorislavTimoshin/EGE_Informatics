with open("24_4544.txt", "r", encoding="utf-8") as file:
    text = file.read()
    maxim = 0
    for j in range(3):
        s = ""
        counter = 0
        for i in range(j, len(text)):
            if "XIX" in (s + text[i]):
                counter = 2
                s = s[-1] + text[i]
            else:
                counter += 1
                s += text[i]
                maxim = max(maxim, counter)
    print(maxim)
