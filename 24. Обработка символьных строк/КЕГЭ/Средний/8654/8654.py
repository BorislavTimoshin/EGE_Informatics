from re import split

with open("24_8654.txt", "r", encoding="utf-8") as file:
    text = file.read()
    # Важно проверять итоговую строку в файле
    words = split(r"[A-Z]B[A-Z]{2}D", text)
    maxim = max(words, key=len)
    print(len(maxim) + 8)

    # Или

    maxim = 0
    back = 0
    for i in range(len(text) - 4):
        maxim = max(maxim, i - back + 1)
        if text[i + 1] + text[i + 4] == "BD":
            maxim = max(maxim, i + 3 - back + 1)
            back = i + 1
    print(maxim)
