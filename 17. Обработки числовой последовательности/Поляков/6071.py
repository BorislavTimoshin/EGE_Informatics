def f1(n1, n2, n3):
    if n1 == n2 and n2 != n3:
        return 2
    if n1 == n3 and n3 != n2:
        return 1
    if n2 == n3 and n2 != n1:
        return 0


def f2(n1, n2, n3):
    if f1(n1, n2, n3) is not None:
        if n1 > minim_40 and n2 > minim_40 and n3 > minim_40:
            return True
    return False


with open("/home/user/Рабочий стол/ztimosh/17-361.txt", "r", encoding="utf-8") as file:
    numbers = list(map(int, file.readlines()))

minim_40 = min(i for i in numbers if abs(i) % 100 == 40)
maxim_index = 0
counter = 0
for i in range(len(numbers) - 2):
    if f2(numbers[i], numbers[i + 1], numbers[i + 2]):
        counter += 1
        maxim_index = i + f1(numbers[i], numbers[i + 1], numbers[i + 2])

print(counter, maxim_index + 1)
