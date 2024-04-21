from math import ceil

# https://education.yandex.ru/ege/task/33086ce1-73ee-4621-a158-c9344f666df8

B = range(5, 23)
lst = []
numbers = [0.5 * i for i in range(60)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                if (not (5 <= x <= 22)) and (a1 <= x <= a2):
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(max(lst))
