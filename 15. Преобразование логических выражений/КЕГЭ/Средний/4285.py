from math import ceil

P = range(25, 241)
Q = range(175, 301)
R = range(270, 341)
lst = []
numbers = [0.5 * i for i in range(800)]

for a1 in numbers:
    for a2 in numbers:
        if a2 >= a1:
            flag = True
            for x in numbers:
                f = ((175 <= x <= 300) <= (25 <= x <= 240)) or ((not(a1 <= x <= a2)) <= (270 <= x <= 340))
                if not f:
                    flag = False
                    break
            if flag:
                lst.append(ceil(a2) - int(a1))

print(min(lst))
