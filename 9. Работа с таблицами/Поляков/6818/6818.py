import csv
from collections import Counter

with open("9-226.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        c = Counter(numbers)
        vals = list(c.values())
        if vals.count(2) == 2 and vals.count(1) == 3:
            maxim = max(numbers)
            if c[maxim] == 1:
                print(sum(numbers))
                exit()
