from re import fullmatch

with open("24_8510.txt", "r", encoding="utf-8") as file:
    text = file.read()
    maxim = 0
    k = 0
    for i in range(len(text)):
        ss = text[i:i+2]
        if fullmatch(r"[NOP]{2}", ss):
            maxim = max(maxim, k + 1)
            k = -1
        k += 1
        maxim = max(maxim, k)
    print(maxim)
