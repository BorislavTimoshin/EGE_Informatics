def f(n1, n2, n3):
    c = 0
    if len(str(abs(n1))) == 4:
        c += 1
    if len(str(abs(n2))) == 4:
        c += 1
    if len(str(abs(n3))) == 4:
        c += 1
    if c <= 2:
        return True
    return False


with open("/home/user/Рабочий стол/ztimosh/17-380.txt", "r", encoding="utf-8") as file:
    numbers = list(map(int, file.readlines()))

maxim_25 = max(i for i in numbers if abs(i) % 100 == 25)
max_sum = -100000000000000
counter = 0

for i in range(len(numbers) - 2):
    if f(numbers[i], numbers[i + 1], numbers[i + 2]):
        summa = numbers[i] + numbers[i + 1] + numbers[i + 2]
        if summa <= maxim_25:
            counter += 1
            if summa > max_sum:
                max_sum = summa
print(counter, max_sum)
