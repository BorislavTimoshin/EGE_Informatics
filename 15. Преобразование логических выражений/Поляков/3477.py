def f(x, a):
    return (not((x in {2, 4, 9, 10, 15}) == (x in a))) <= ((x in {3, 8, 9, 10, 20}) == (x in a))


A = set()
for x in [0.5 * i for i in range(2000)]:
    if f(x, A) == 0:
        A.add(x)
print(A)
print(9 * 10)
