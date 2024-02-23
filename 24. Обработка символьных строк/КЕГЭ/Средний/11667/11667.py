with open("24_11667.txt", "r", encoding="utf-8") as file:
    text = file.read()
    k = 0
    l = 0
    maxim = 0
    for i in range(7, len(text)):
        if text[i-7:i+1] == "INFINITY":
            k += 1
        while k == 1001:
            if text[l:l+8] == "INFINITY":
                k -= 1
            l += 1
        if k == 1000:
            maxim = max(maxim, i - l + 1)
    print(maxim)
