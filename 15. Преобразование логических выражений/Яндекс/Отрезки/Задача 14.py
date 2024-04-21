from math import ceil

# https://education.yandex.ru/ege/task/b2f81f25-7171-4e9a-8456-607bca827919

P = range(23, 45)
Q = range(34, 57)
lst = []
numbers = [0.5 * i for i in range(200)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                f = ((x < a1) or (x > a2)) or ((x < 23) or (x >= 45)) and (34 <= x <= 56)
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(max(lst))
