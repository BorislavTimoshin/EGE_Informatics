def f(n1, n2, n3):
    c = 0
    if 100 <= n1 <= 999:
        c += 1
    if 100 <= n2 <= 999:
        c += 1
    if 100 <= n3 <= 999:
        c += 1
    if c == 2:
        return True


with open("/home/user/Рабочий стол/ztimosh/17_2024.txt", "r", encoding="utf-8") as file:
    numbers = list(map(int, file.readlines()))

maxim_13 = max(i for i in numbers if i % 100 == 13)
counter = 0
max_sum = 0

for i in range(len(numbers) - 2):
    if f(numbers[i], numbers[i + 1], numbers[i + 2]):
        summa = numbers[i] + numbers[i + 1] + numbers[i + 2]
        if summa <= maxim_13:
            counter += 1
            if summa > max_sum:
                max_sum = summa
print(counter, max_sum)
