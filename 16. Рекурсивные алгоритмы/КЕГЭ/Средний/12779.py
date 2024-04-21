def f(n):
    global x
    if n >= 3000:
        return n
    if n < 3000:
        return n + x + f(n + 2)


for x in range(-100000, 1000000):
    if f(2984) - f(2988) == 5916:
        print(x)
