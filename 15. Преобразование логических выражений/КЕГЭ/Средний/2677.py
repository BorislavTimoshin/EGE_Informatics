from math import ceil

D = range(12, 21)
C = range(31, 46)
lst = []
numbers = [0.5 * i for i in range(100)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                dd = 12 <= x <= 20
                cc = 31 <= x <= 45
                aa = a1 <= x <= a2
                f = (not cc) and (not dd) or ((dd or cc) <= aa)
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
