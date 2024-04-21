from math import ceil

P = range(5, 55)
Q = range(50, 94)
lst = []
numbers = [i for i in range(-300, 300)]

for A in range(-1000, 10000):
    counter = 0
    for x in numbers:
        pp = 5 <= x <= 54
        qq = 50 <= x <= 93
        f = ((not pp) and qq) <= (x > A)
        if not f:
            counter += 1
    if counter == 20:
        print(A)
        break
