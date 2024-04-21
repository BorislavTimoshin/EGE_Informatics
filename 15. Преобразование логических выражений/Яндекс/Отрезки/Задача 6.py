from math import ceil

# https://education.yandex.ru/ege/task/f1912e9d-bfea-448f-bf17-96b14e7f7b44

B = range(101, 144)
C = range(144, 200)
lst = []
numbers = [0.5 * i for i in range(500)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                if (a1 <= x <= a2) <= ((101 <= x <= 143) or (144 <= x <= 199)):
                    pass
                else:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(max(lst))
