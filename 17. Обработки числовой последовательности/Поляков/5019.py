def f(n1, n2):
    if n1 > sum_7 and n2 > sum_7:
        return True
    return False


with open("/home/user/Рабочий стол/ztimosh/17-278.txt", "r", encoding="utf-8") as file:
    numbers = list(map(int, file.readlines()))

sum_7 = "".join(map(oct, numbers)).count("7") * 7
counter = 0
minim = 10000000

for i in range(len(numbers) - 1):
    if f(numbers[i], numbers[i + 1]):
        counter += 1
        if numbers[i] + numbers[i + 1] < minim:
            minim = numbers[i] + numbers[i + 1]
print(counter, minim)
