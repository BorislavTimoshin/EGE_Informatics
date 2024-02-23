from re import search

with open("24_2502.txt", "r", encoding="utf-8") as file:
    text = file.readlines()
    counter = 0
    for i in text:
        if search("K.GE", i):
            counter += 1
    print(counter)
