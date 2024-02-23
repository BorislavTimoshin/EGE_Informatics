with open("24_13085.txt", "r", encoding="utf-8") as file:
    text = file.read()
    kx = 0
    ky = 0
    maxim = 0
    l = 0
    r = 0
    while r < len(text):
        while kx <= 1 and ky <= 1:
            maxim = max(maxim, r - l + 1)
            r += 1
            if r == len(text):
                break
            if text[r] == "X":
                kx += 1
            if text[r] == "Y":
                ky += 1
        while not (kx <= 1 and ky <= 1):
            if text[l] == "X":
                kx -= 1
            if text[l] == "Y":
                ky -= 1
            l += 1
    print(maxim)
    maxim = max(maxim, r - l + 1)
    print(maxim)
