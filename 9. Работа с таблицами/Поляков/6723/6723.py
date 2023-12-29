import csv
from collections import Counter

counter = 0
with open("9-223.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        c = Counter(numbers)
        vals = list(c.values())
        keys = list(c.keys())
        if vals.count(3) == 1 and vals.count(1) == 4:
            ind = vals.index(3)
            key = keys[ind]
            keys.remove(key)
            if sum(keys) / len(keys) <= key:
                counter += 1
print(counter)
