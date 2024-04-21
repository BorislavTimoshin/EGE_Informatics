from math import ceil

P = range(1, 99)
Q = range(25, 43)
lst = []
numbers = [0.5 * i for i in range(200)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                f = (25 <= x <= 42) <= ((not (1 <= x <= 98)) and (25 <= x <= 42) <= (a1 <= x <= a2))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

try:
    print(min(lst))
except ValueError:
    print(0)
