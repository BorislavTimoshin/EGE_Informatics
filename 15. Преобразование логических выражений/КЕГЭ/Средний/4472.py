from math import ceil

P = range(254, 801)
Q = range(410, 824)
lst = []
numbers = [0.5 * i for i in range(2000)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                f = ((254 <= x <= 800) and (x < a1 or x > a2)) <= (410 <= x <= 823)
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
