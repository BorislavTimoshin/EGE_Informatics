from re import findall

with open("24_9791.txt", "r", encoding="utf-8") as file:
    text = file.read()
    ss = findall("[A-F1-9]+", text)
    print(len(max(ss, key=len)))
    maxim = 0
    s = ""
    for i in range(len(text)):
        if text[i] in "ABCDEF123456789":
            s += text[i]
        else:
            maxim = max(maxim, len(s))
            s = ""
    print(maxim)
