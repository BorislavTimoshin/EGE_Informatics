def f(x, a):
    P = x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = x in {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
    return ((x in a) <= (not P)) and ((not Q) <= (not (x in a)))


A = set()
for x in [0.5 * i for i in range(2000)]:
    A.add(x)
    if f(x, A) == 0:
        A.remove(x)
print(A)
print(len(A))
