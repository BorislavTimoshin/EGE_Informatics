P = range(10, 23)
Q = range(20, 37)


def f(x, A):
    return (x in P) <= (x not in Q or x in A)


A = set()
for x in range(1, 10001):
    if not f(x, A):
        A.add(x)

print(A)
# Ответ 22 - 20 = 2
