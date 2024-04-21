from math import ceil

P = range(117, 159)
Q = range(129, 181)
lst = []
numbers = [0.5 * i for i in range(200, 400)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                pp = 117 <= x <= 158
                qq = 129 <= x <= 180
                aa = a1 <= x <= a2
                f = pp <= ((qq and (not aa)) <= (not pp))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
