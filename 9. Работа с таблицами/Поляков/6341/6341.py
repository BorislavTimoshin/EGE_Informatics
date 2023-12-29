import csv

counter = 0
d = {}
with open("9-204.csv", "r", encoding="utf-8-sig") as file:
    reader = list(csv.reader(file, delimiter=";"))
    for i in reader:
        numbers = list(map(int, i))
        for j in numbers:
            if d.get(j) is not None:
                d[j] += 1
            else:
                d[j] = 1
    for i in reader:
        numbers = list(map(int, i))
        for j in numbers:
            if numbers.count(j) > 1:
                if (d[j] - numbers.count(j)) % 2 == 1:
                    counter += 1
                    break
print(counter)
