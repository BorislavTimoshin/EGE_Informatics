from math import ceil

# https://education.yandex.ru/ege/task/219c0d8e-bf34-4ec2-8f11-cf4d06a6fae7

B = range(15, 41)
C = range(21, 64)
lst = []
numbers = [0.5 * i for i in range(200)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                bb = 15 <= x <= 40
                cc = 21 <= x <= 63
                f = (not bb) <= ((cc and (not (a1 <= x <= a2))) <= bb)
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
