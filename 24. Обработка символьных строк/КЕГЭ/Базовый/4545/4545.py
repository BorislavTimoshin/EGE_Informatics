with open("24_4545.txt", "r", encoding="utf-8") as file:
    text = file.read()
    maxim = 0
    for j in range(3):
        counter = 0
        for i in range(j, len(text), 3):
            s = text[i:i+3]
            if s == "XYZ" or s == "ZYX":
                counter += 1
                maxim = max(maxim, counter)
            else:
                counter = 0
    print(maxim)
