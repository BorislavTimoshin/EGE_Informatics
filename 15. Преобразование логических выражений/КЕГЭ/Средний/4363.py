from math import ceil

A = range(30, 51)
P = range(10, 81)
lst = []
numbers = [0.5 * i for i in range(200)]

for q1 in numbers:
    for q2 in numbers:
        if q2 >= q1:
            flag = True
            for x in numbers:
                f = (q1 <= x <= q2) <= ((30 <= x <= 50) and (not (10 <= x <= 80)))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(q2) - int(q1))

try:
    print(min(lst))
except ValueError:
    print(0)
