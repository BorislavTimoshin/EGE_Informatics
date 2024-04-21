def f(x, a):
    P = {1, 3, 7}
    Q = {1, 2, 4, 5, 6}
    return ((x not in a) <= (x not in P)) or ((x not in Q) and (x in P))


A = set()
for x in [0.5 * i for i in range(2000)]:
    if f(x, A) == 0:
        A.add(x)
print(A)
print(len(A))
