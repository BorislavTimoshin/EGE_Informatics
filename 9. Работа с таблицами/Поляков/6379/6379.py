import csv

counter = 0
with open("9-209.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        maxim = max(numbers)
        minim = min(numbers)
        if len(numbers) == len(set(numbers)):
            sor = sorted(numbers)
            if sor[2] * 2 > maxim and sor[2] * 2 > 3 * minim:
                counter += 1
print(counter)
