def f(x, a):
    P = {1, 2, 3, 4, 5, 6}
    Q = {3, 5, 15}
    return (x not in a) <= ((x not in P) and (x in Q)) or (x not in Q)


A = set()
for x in [0.5 * i for i in range(2000)]:
    if f(x, A) == 0:
        A.add(x)
print(A)
print(len(A))
