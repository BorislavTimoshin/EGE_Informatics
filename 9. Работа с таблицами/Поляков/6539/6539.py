import csv
from itertools import permutations

counter = 0
with open("9-214.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        if len(numbers) == len(set(numbers)):
            for j in permutations(numbers):
                if (j[0] + j[1]) / 2 == (j[2] + j[3]) / 2 == j[4]:
                    counter += 1
                    break
print(counter)
