from re import findall

with open("24_2478.txt", "r", encoding="utf-8") as file:
    text = file.read()
    # sequences = findall(r"G.ME", text)
    # print(len(sequences))
    #

counter = 0
s = ""
maxim = 0
for i in range(len(text)):
    t = s[-2:] + text[i]
    if len(set(t)) == 1 and len(t) == 3:
        counter = 2
        s = s[-1] + text[i]
    else:
        counter += 1
        s += text[i]
        maxim = max(maxim, counter)
print(maxim)
