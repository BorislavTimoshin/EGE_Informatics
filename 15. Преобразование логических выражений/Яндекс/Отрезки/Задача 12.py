from math import ceil

# https://education.yandex.ru/ege/task/f21ffc71-18b2-48d5-a4b3-5286316264af

P = range(3, 88)
Q = range(50, 73)
lst = []
numbers = [0.5 * i for i in range(200)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                pp = 3 <= x <= 87
                qq = 50 <= x <= 72
                aa = a1 <= x <= a2
                f = pp and (not (aa == qq)) or (not (qq or aa))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(max(lst))
