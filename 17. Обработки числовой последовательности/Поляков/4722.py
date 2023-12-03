def f(n1, n2):
    c = 0
    end = False
    if n1 > sum_35:
        c += 1
        if hex(n2)[2:].endswith("ef"):
            end = True
    if n2 > sum_35:
        c += 1
        if hex(n1)[2:].endswith("ef"):
            end = True
    if c == 1 and end:
        return True
    return False


with open("/home/user/Рабочий стол/ztimosh/17-243.txt", "r", encoding="utf-8") as file:
    numbers = list(map(int, file.readlines()))

sum_35 = sum(sum(map(int, str(i))) for i in numbers if i % 35 == 0)
counter = 0
minim = 1000000000
for i in range(len(numbers) - 1):
    if f(numbers[i], numbers[i + 1]):
        counter += 1
        if numbers[i] + numbers[i + 1] < minim:
            minim = numbers[i] + numbers[i + 1]
print(counter, minim)
