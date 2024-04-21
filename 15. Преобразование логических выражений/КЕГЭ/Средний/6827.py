from math import ceil

P = range(257, 1001)
Q = range(5, 101)
R = range(99, 259)
lst = []
numbers = [0.5 * i for i in range(2040)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                f = ((a1 <= x <= a2) <= (99 <= x <= 258)) and ((not((a1 <= x <= a2) <= (257 <= x <= 1000))) <= (5 <= x <= 100))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
