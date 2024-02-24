with open("24_10105.txt", "r", encoding="utf-8") as file:
    text = file.read()
    l = 0
    k = 0
    maxim = 0
    for i in range(len(text)):
        if text[i] == "T":
            k += 1
        while k == 101:
            if text[l] == "T":
                k -= 1
            l += 1
        if k == 100:
            maxim = max(maxim, i - l + 1)
    print(maxim)
