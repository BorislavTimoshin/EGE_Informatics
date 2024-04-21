from math import ceil


def dell(n, m):
    return n % m == 0


P = range(257, 357)
Q = range(5, 601)
R = range(59, 229)
lst = []
numbers = [0.5 * i for i in range(1250)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in range(1, 650):
                pp = 257 <= x <= 356
                qq = 5 <= x <= 600
                rr = 59 <= x <= 228
                aa = a1 <= x <= a2
                f = (rr <= aa) or ((dell(x, 3) <= pp) <= (qq <= aa))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
