def f(x, a):
    P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
    return ((x in P) <= (x in a)) or ((x not in a) <= (x not in Q))


A = set()
for x in [0.5 * i for i in range(2000)]:
    if f(x, A) == 0:
        A.add(x)
print(A)
print(len(A))
