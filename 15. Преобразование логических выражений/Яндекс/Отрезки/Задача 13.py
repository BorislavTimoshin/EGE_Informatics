from math import ceil

# https://education.yandex.ru/ege/task/42f2f42f-16cf-4453-a8bf-26afaba65c51

P = range(10, 28)
Q = range(20, 41)
R = range(32, 51)
lst = []
numbers = [0.5 * i for i in range(200)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                f = (not (a1 <= x <= a2)) or (20 <= x <= 40) and ((10 <= x <= 27) or (32 <= x <= 50))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(max(lst))
