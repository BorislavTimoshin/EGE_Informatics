import csv
from collections import Counter

counter = 0


def f1(lst):
    cc = Counter(lst)
    vl = list(cc.values())
    if vl.count(2) == 1 and vl.count(1) == 3:
        return True
    return False


def f2(lst):
    sum0 = 0
    sum1 = 0
    for ii in lst:
        if ii % 2 == 0:
            sum0 += ii
        else:
            sum1 += ii
    return sum1 > sum0


with open("9-221.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        if f1(numbers) + f2(numbers) == 1:
            counter += 1
print(counter)
