from math import ceil

P = range(10, 21)
Q = range(35, 46)
lst = []
numbers = [0.5 * i for i in range(100)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                pp = 10 <= x <= 20
                qq = 35 <= x <= 45
                aa = a1 <= x <= a2
                f = ((not pp) <= qq) and (not aa)
                if f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
