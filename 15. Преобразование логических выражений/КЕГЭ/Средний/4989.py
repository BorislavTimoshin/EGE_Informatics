from math import ceil


def dell(n, m):
    return n % m == 0


B = range(20, 81)
lst = []
numbers = [i for i in range(100)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                f = (20 <= x <= 80) <= (dell(x, 17) <= (a1 <= x <= a2))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
