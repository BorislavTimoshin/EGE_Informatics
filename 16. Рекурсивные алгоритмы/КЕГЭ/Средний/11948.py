from math import sqrt


def f(n):
    return g(n - 1)


def g(n):
    if n < 10:
        return n
    return g(n - 2) + 1


counter = 0
for x in range(1, 101):
    res = f(x)
    if res > 0:
        if sqrt(res).is_integer():
            counter += 1

print(counter)
