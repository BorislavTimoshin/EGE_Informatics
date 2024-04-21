from math import ceil

P = range(106, 219)
Q = range(132, 389)
R = range(183, 257)
lst = []
numbers = [0.5 * i for i in range(200, 800)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                pp = 106 <= x <= 218
                qq = 132 <= x <= 388
                rr = 183 <= x <= 256
                aa = a1 <= x <= a2
                f = (not (qq <= (pp or rr))) <= ((not aa) <= (not qq))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
