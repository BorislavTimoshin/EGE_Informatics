import csv
from collections import Counter

counter = 0
with open("9-224.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        c = Counter(numbers)
        vals = list(c.values())
        if vals.count(2) == 2:
            for k, j in c.items():
                if j == 1:
                    numbers.remove(k)
                    sort_numbers = sorted(set(numbers))
                    if sort_numbers[0] < k < sort_numbers[1]:
                        counter += 1
print(counter)
