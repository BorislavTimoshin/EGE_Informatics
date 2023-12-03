def arif(n1, n2, n3):
    if n3 > n2 > n1:
        if n3 - n2 == n2 - n1:
            return n2 - n1
    return False


def geo(n1, n2, n3):
    if n3 > n2 > n1:
        if n2 ** 2 == n1 * n3:
            return n2 / n1
    return False


def f(n1, n2, n3, n4, n5, n6):
    a, b = arif(n1, n2, n3), geo(n4, n5, n6)
    if a and b:
        return a == b
    c, d = geo(n1, n2, n3), arif(n4, n5, n6)
    if c and d:
        return c == d
    return False


with open("/home/user/Рабочий стол/ztimosh/17-281.txt", 'r', encoding="utf-8") as file:
    numbers = list(map(int, file.readlines()))

counter = 0
max_sum = 0
for i in range(len(numbers) - 5):
    if f(numbers[i], numbers[i + 1], numbers[i + 2], numbers[i + 3], numbers[i + 4], numbers[i + 5]):
        counter += 1
        summa = numbers[i] + numbers[i + 1] + numbers[i + 2] + numbers[i + 3] + numbers[i + 4] + numbers[i + 5]
        if summa > max_sum:
            max_sum = summa
print(counter, max_sum)
