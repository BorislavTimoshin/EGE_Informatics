from re import split

with open("24-280.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = split("[XY]", text)  # Делим текст на подпоследовательности символов с помощью разделитей букв X или Y
    maxim = 0
    for i in range(len(sequences) - 5):
        # Находим каждые 6 подпоследовательностей и соединяем в единую строку
        result = "".join(sequences[i:i+6])
        maxim = max(maxim, len(result))
    print(maxim + 5)  # Прибавляем 5 символов X или Y

# Или

with open("24-280.txt", "r", encoding="utf-8") as file:
    text = file.read()
    k = 0
    l = 0
    maxim = 0
    for r in range(len(text)):
        if text[r] == "X" or text[r] == "Y":
            k += 1
        while k == 6:
            if text[l] == "X" or text[l] == "Y":
                k -= 1
            l += 1
        if k <= 5:
            maxim = max(maxim, r - l + 1)
    print(maxim)
