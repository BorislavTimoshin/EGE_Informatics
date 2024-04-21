from math import ceil

P = range(1, 40)
Q = range(23, 59)
lst = []
numbers = [0.5 * i for i in range(200)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                f = ((1 <= x <= 39) <= (not (23 <= x <= 58))) <= (not (a1 <= x <= a2))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(max(lst))
