from math import ceil

# https://education.yandex.ru/ege/task/219c0d8e-bf34-4ec2-8f11-cf4d06a6fae7

B = range(23, 38)
C = range(41, 74)
lst = []
numbers = [0.5 * i for i in range(200)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                f = not (((not (23 <= x <= 37)) <= (41 <= x <= 73)) <= (a1 <= x <= a2))
                if f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
