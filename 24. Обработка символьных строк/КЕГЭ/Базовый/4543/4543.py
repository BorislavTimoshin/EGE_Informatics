with open("24_4543.txt", "r", encoding="utf-8") as file:
    text = file.read()
    maxim = 0
    for j in range(5):
        counter = 0
        s = ""
        for i in range(len(text)):
            if "XVIII" in (s + text[i]):
                counter = 4
                s = s[-3:] + text[i]
            else:
                counter += 1
                s += text[i]
                maxim = max(maxim, counter)
    print(maxim)
