from math import ceil

P = range(13, 20)
Q = range(17, 24)
lst = []
numbers = [0.5 * i for i in range(60)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                pp = 13 <= x <= 19
                qq = 17 <= x <= 23
                f = (not ((not pp) <= qq)) <= ((a1 <= x <= a2) <= ((not qq) <= pp))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(max(lst))
