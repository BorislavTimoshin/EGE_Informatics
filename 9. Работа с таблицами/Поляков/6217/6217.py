import csv
from collections import Counter

counter = 0
with open("9-200.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        d = Counter(numbers)
        vals = list(d.values())
        if vals.count(2) == 3:
            sorted_numbers = sorted(set(numbers))
            if sorted_numbers[0] ** 2 + sorted_numbers[1] ** 2 == sorted_numbers[2] ** 2:
                counter += 1
print(counter)
