from re import findall


with open("24_2250.txt", "r", encoding="utf-8") as file:
    text = file.read()
    # sequences = findall(r"[^D]*D?[^D]*D?[^D]*", text)

lst = []
for i, sym in enumerate(text):
    if sym == "A":
        lst.append(i)

counter = 0
maxim = 0
for i in range(len(lst) - 2):
    counter = lst[i+2] - lst[i] - 1
    maxim = max(maxim, counter)
print(maxim)
