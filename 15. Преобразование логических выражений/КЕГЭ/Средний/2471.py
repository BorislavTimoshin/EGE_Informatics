from math import ceil

P = range(1, 41)
Q = range(25, 121)
lst = []
numbers = [0.5 * i for i in range(300)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                pp = 1 <= x <= 40
                qq = 25 <= x <= 120
                aa = a1 <= x <= a2
                f = qq <= (((not pp) and qq) <= aa)
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
