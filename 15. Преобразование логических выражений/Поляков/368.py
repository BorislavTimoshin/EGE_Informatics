def f(x, a):
    P = {2, 4, 6, 8, 10, 12}
    Q = {4, 8, 12, 116}
    return (x in P) <= (((x in Q) and (x not in a)) <= (x not in P))


A = set()
for x in [0.5 * i for i in range(2000)]:
    if f(x, A) == 0:
        A.add(x)
print(A)
print(sum(A))
