import csv

counter = 0
with open("9-215.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        maxim = max(numbers)
        minim = min(numbers)
        numbers.remove(maxim)
        numbers.remove(minim)
        if abs(numbers[0] * numbers[1]) % minim == 0:
            counter += 1
print(counter)
