from math import ceil

# https://education.yandex.ru/ege/task/6d3bdf4a-126c-4574-9079-40738cf699b3

B = range(10, 22)
lst = []
numbers = [0.5 * i for i in range(60)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                if (not (10 <= x <= 21)) or (a1 <= x <= a2):
                    pass
                else:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
