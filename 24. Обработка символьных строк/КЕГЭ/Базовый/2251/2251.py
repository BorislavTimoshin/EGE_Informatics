with open("24_2251.txt", "r", encoding="utf-8") as file:
    text = file.read()

lst = []
for i, sym in enumerate(text):
    if sym == "D":
        lst.append(i)
maxim = 0
for i in range(len(lst) - 3):
    count = lst[i + 3] - lst[i] - 1
    maxim = max(maxim, count)
print(maxim)
