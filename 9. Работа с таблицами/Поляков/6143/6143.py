import csv
from collections import Counter


def f1(lst):
    c = Counter(lst)
    vals = list(c.values())
    if vals.count(2) == 1 and vals.count(1) == 3:
        return True
    return False


def f2(lst):
    c = Counter(lst)
    vals = list(c.values())
    keys = list(c.keys())
    ind = vals.index(2)
    key = keys[ind]
    keys.remove(key)
    if key * 2 > sum(keys):
        return True
    return False


counter = 0

with open("9-194.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        if f1(numbers):
            if f2(numbers):
                counter += 1

print(counter)
