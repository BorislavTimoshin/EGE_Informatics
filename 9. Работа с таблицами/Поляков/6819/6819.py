import csv
from collections import Counter

counter = 0
with open("9-227.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        vals = list(Counter(numbers).values())
        if vals.count(2) == 1:
            sort = sorted(numbers)
            if sort[2] + sort[3] > 2 * (sort[0] + sort[1]):
                if max(numbers) % min(numbers) != 0:
                    counter += 1
print(counter)
