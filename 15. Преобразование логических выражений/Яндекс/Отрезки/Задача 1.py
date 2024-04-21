from math import ceil

# https://education.yandex.ru/ege/task/9ff6dee9-7b77-4354-a417-ac59a1d8399a

B = range(10, 24)
C = range(12, 31)
lst = []
numbers = [0.5 * i for i in range(100)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                if (not (10 <= x <= 23)) or (a1 <= x <= a2) or (not (12 <= x <= 30)):
                    pass
                else:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
