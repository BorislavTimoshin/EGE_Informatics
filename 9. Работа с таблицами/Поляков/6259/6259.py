import csv
from collections import Counter

counter = 0
with open("9-201.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        d = Counter(numbers)
        vals = list(d.values())
        if vals.count(3) == 1 and vals.count(1) == 3:
            v = 0
            sum_not_p = []
            for k, j in d.items():
                if j == 1:
                    sum_not_p.append(k)
                else:
                    v = k
            if sum(sum_not_p) / len(sum_not_p) < v * 3:
                counter += 1
print(counter)
