from math import ceil

P = range(5, 41)
Q = range(41, 55)
R = range(6, 54)
lst = []
numbers = [0.5 * i for i in range(200)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                f = ((x < 5 or x > 40) <= (41 <= x <= 54)) and (6 <= x <= 53) and (x < a1 or x > a2)
                if f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
