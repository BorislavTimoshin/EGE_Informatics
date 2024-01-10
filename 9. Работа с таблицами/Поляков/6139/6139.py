import csv
from collections import Counter


def f1(lst):
    c = Counter(lst)
    vals = list(c.values())
    if 0 < vals.count(1) < 5:
        return True
    return False


def f2(lst):
    povtor = []
    nepovtor = []
    for num in lst:
        if lst.count(num) == 1:
            nepovtor.append(num)
        else:
            povtor.append(num)
    if len(povtor) and len(nepovtor):
        return (sum(povtor) / len(povtor)) == (sum(nepovtor) / len(nepovtor))
    return False


counter = 0

with open("9-191.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        if f1(numbers) + f2(numbers) == 2:
            counter += 1

print(counter)
