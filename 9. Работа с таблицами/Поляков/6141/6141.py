import csv


def f1(lst):
    count_0 = sum(map(lambda x: x % 2 == 0, lst))
    count_1 = sum(map(lambda x: x % 2 == 1, lst))
    if count_0 < count_1:
        return True
    return False


def f2(lst):
    sum0 = sum(filter(lambda x: x % 2 == 0, lst))
    sum1 = sum(filter(lambda x: x % 2 == 1, lst))
    if sum0 > sum1:
        return True
    return False


counter = 0

with open("9-194.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        if len(numbers) == len(set(numbers)):
            if f1(numbers) + f2(numbers) == 2:
                counter += 1

print(counter)
