from math import ceil


def dell(n, m):
    return n % m == 0


B = range(10, 41)
lst = []
numbers = [0.5 * i for i in range(100)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                f = (a1 <= x <= a2) or ((10 <= x <= 40) <= (not dell(x, 6)))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
