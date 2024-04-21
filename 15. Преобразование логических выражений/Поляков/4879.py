def f(x, a):
    P = x in {1, 2, 4, 8}
    Q = x in {1, 2, 3, 4, 5, 6}
    return (not (x in a)) <= (not (P or Q))


A = set()
for x in [0.5 * i for i in range(2000)]:
    if f(x, A) == 0:
        A.add(x)
print(A)
print(len(A))
