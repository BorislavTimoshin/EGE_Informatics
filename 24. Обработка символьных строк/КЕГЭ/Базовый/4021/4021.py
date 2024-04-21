with open("24_4021.txt", "r", encoding="utf-8") as file:
    text = file.read()
    words = text.split(".")
    maxim = 0
    max_d = []
    for i in range(len(words) - 5):
        d = words[i:i+6]
        if len("".join(d)) > maxim:
            max_d = d
        maxim = max(maxim, len("".join(d)))
    print(maxim + 5)
