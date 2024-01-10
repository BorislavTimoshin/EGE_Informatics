import csv


def f1(lst):
    return len(list(filter(lambda x: x % 3 == 0, lst))) == 3


def f2(lst):
    summa = sum(filter(lambda x: x % 3 == 0, lst))
    maxim = max(lst)
    minim = min(lst)
    if maxim - minim <= summa:
        return True
    return False


counter = 0

with open("9-198.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i[:6]))
        if f1(numbers) + f2(numbers) == 2:
            counter += 1

print(counter)
