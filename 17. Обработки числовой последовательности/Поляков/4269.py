def f(n1, n2):
    if n1 % 7 == 0 and n2 % 17 != 0:
        return True
    return False


minim = 30000
counter = 0
with open("/home/user/Рабочий стол/ztimosh/17-1.txt", "r", encoding="utf-8") as file:
    numbers = list(map(int, file.readlines()))

for i in range(len(numbers) - 1):
    if f(numbers[i], numbers[i + 1]) or f(numbers[i + 1], numbers[i]):
        counter += 1
        if numbers[i] + numbers[i + 1] < minim:
            minim = numbers[i] + numbers[i + 1]

print(counter, minim)
