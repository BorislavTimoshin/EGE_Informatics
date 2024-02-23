with open("24_5223.txt", "r", encoding="utf-8") as file:
    text = file.read()
    s = ""
    counter = 0
    maxim = 0
    for i in range(len(text)):
        if "DD" in s + text[i]:
            counter = 1
            s = text[i]
        else:
            counter += 1
            s += text[i]
            if "FE" in s:
                maxim = max(maxim, counter)
    print(maxim)
