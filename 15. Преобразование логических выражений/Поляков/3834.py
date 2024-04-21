def dell(n, m):
    return n % m == 0


def f(A, x):
    return dell(A, 9) and (dell(280, x) <= ((not dell(A, x)) <= (not dell(730, x))))


for a in range(1, 1000):
    if all(f(a, X) for X in range(1, 1000)):
        print(a)
        break
