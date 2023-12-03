def f(n1, n2):
    if (n1 % 2 == 0 and n2 % 2 == 1) or (n2 % 2 == 0 and n1 % 2 == 1):
        if n1 % 2 == 0:
            if n1 % 4 == 0 and n2 % 11 == 0:
                return True
        if n2 % 2 == 0:
            if n2 % 4 == 0 and n1 % 11 == 0:
                return True
            return False


counter = 0
maxim = -300000
with open("/home/user/Рабочий стол/ztimosh/17-3.txt", "r", encoding="utf-8") as file:
    numbers = list(map(int, file.readlines()))

for i in range(len(numbers) - 1):
    if f(numbers[i], numbers[i + 1]) or f(numbers[i + 1], numbers[i]):
        counter += 1
        if numbers[i] + numbers[i + 1] > maxim:
            maxim = numbers[i] + numbers[i + 1]
print(counter, maxim)
