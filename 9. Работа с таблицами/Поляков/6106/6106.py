import csv


def f1(lst):
    if len(lst) != len(set(lst)):
        return True
    return False


def f2(lst):
    c = 0
    for j in lst:
        if j % 2 == 1:
            c += 1
    return c == 3


counter = 0

with open("9-190.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        if f1(numbers) + f2(numbers) == 1:
            counter += 1

print(counter)
