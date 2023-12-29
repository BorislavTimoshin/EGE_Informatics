import csv
from collections import Counter

with open("9-222.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i, numbers in enumerate(reader, 1):
        numbers = list(map(int, numbers))
        c = Counter(numbers)
        vals = list(c.values())
        keys = list(c.keys())
        if vals.count(2) == 1 and vals.count(1) == 4:
            ind = vals.index(2)
            key = keys[ind]
            keys.remove(key)
            if key >= sum(keys) / len(keys):
                print(i)
                exit()
