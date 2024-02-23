from re import findall

with open("24_11813.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:[AOEIUY][^AOEIUY])+", text)
    print(max(sequences, key=len))
    print(len("OFAWUTITASAVEXEPESEDITIH") + 1)

# Или

counter = 1
maxim = 1
for i in range(len(text) - 1):
    if (text[i] in 'AOEIUY') != (text[i + 1] in "AOEIUY"):
        counter += 1
        maxim = max(maxim, counter)
    else:
        counter = 1
print(maxim)
