def f(x, a):
    P = x in {1, 12}
    Q = x in {12, 13, 14, 15, 16}
    return (not (x in a)) <= ((not P) and (not Q))


A = set()
for x in [0.5 * i for i in range(2000)]:
    if f(x, A) == 0:
        A.add(x)
print(A)
print(len(A))
