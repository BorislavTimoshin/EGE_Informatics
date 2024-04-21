from math import ceil

P = range(5, 281)
Q = range(295, 401)
R = range(375, 451)
lst = []
numbers = [0.5 * i for i in range(1000)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                f = ((295 <= x <= 400) <= (5 <= x <= 280)) or ((not(a1 <= x <= a2)) <= (375 <= x <= 450))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
