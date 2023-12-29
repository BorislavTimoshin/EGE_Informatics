import csv
from collections import Counter


def f1(lst):
    dd = Counter(lst)
    vv = list(dd.values())
    if vv.count(2) == 1 and vv.count(1) == 4:
        return True
    return False


def f2(lst):
    even = []
    not_even = []
    for ii in lst:
        if ii % 2 == 0:
            even.append(ii)
        else:
            not_even.append(ii)
    if not even:
        srednee1 = 0
    else:
        srednee1 = sum(even) / len(even)
    if not not_even:
        srednee2 = 0
    else:
        srednee2 = sum(not_even) / len(not_even)
    if abs(srednee1 - srednee2) > 50:
        return True
    return False


counter = 0

with open("9-199.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        if f1(numbers) + f2(numbers) == 1:
            counter += 1

print(counter)
