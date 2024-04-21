from math import ceil

# https://education.yandex.ru/ege/task/ad49b4d3-62dc-420f-aa97-519d891a80f5

P = range(20, 68)
Q = range(33, 99)
lst = []
numbers = [0.5 * i for i in range(400)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                pp = 20 <= x <= 67
                qq = 33 <= x <= 98
                f = pp <= ((qq and (not (a1 <= x <= a2))) <= (not pp))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
