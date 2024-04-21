from math import ceil

# https://education.yandex.ru/ege/task/8e383cd1-86c7-4ddb-8e69-af16360eb883

P = range(117, 159)
Q = range(129, 181)
lst = []
numbers = [0.5 * i for i in range(400)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                pp = 117 <= x <= 158
                qq = 129 <= x <= 180
                if pp <= ((qq and (not (a1 <= x <= a2))) <= (not pp)):
                    pass
                else:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
