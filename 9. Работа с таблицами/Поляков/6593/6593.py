import csv
from functools import reduce
from operator import mul

counter = 0
with open("9-219.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        maxim = max(numbers)
        numbers.remove(maxim)
        if maxim ** 2 > reduce(mul, numbers):
            maxim2 = max(numbers)
            numbers.remove(maxim2)
            if maxim + maxim2 > 2 * sum(numbers):
                counter += 1
print(counter)
