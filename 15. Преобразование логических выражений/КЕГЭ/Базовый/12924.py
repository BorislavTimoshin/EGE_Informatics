P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
A = set()
for x in range(1000):
    A.add(x)
    if ((x in A) <= (x in P)) and (not(x in Q) <= (not(x in A))):
        pass
    else:
        A.remove(x)
print(len(A))
