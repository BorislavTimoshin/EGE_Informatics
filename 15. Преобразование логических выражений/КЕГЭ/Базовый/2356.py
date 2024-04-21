from math import ceil

P = range(10, 46)
Q = range(35, 79)
lst = []
numbers = [0.5 * i for i in range(200)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                f = ((not(x in P)) <= (x in Q)) and (not(a1 <= x <= a2))
                if f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
