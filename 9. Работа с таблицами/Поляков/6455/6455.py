import csv
from collections import Counter

counter = 0
with open("9-210.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        maxim = max(numbers)
        minim = min(numbers)
        d = Counter(numbers)
        vals = list(d.values())
        if d[minim] == 1 and vals.count(1) != 6:
            summa = 0
            for j in numbers:
                if numbers.count(j) > 1:
                    summa += j
            numbers.remove(maxim)
            numbers.remove(minim)
            if maxim + minim < summa:
                counter += 1
print(counter)
