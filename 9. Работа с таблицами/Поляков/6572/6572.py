import csv

counter = 0
with open("9-218.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        maxim = max(numbers)
        minim = min(numbers)
        if numbers[0] not in [minim, maxim] and numbers[-1] not in [maxim, minim]:
            numbers.remove(maxim)
            numbers.remove(minim)
            if numbers[0] - numbers[1] != 0:
                if (maxim - minim) % (numbers[0] - numbers[1]) == 0:
                    counter += 1
print(counter)
