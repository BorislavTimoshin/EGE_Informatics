import csv

counter = 0
with open("9-220.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    for i in reader:
        numbers = list(map(int, i))
        if (max(numbers) + min(numbers)) % 3 == 0:
            sort_numbers = sorted(numbers)
            if abs(sort_numbers[0] - sort_numbers[1]) == abs(sort_numbers[2] - sort_numbers[3]):
                counter += 1
print(counter)
