import csv
from collections import Counter

counter = 0
with open("9-225.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        vals = list(Counter(numbers).values())
        if vals.count(2) == 1 and vals.count(1) == 3:
            maxim = max(numbers)
            minim = min(numbers)
            numbers.remove(maxim)
            numbers.remove(minim)
            if (maxim + minim) ** 2 < numbers[0] ** 2 + numbers[1] ** 2 + numbers[2] ** 2:
                counter += 1
print(counter)
