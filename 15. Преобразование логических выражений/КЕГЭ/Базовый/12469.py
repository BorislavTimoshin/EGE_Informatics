A = 0
f_usl = 1
for x in [k*0.25 for k in range(-10_000, 10_000)]:
    D = 7 <= x <= 68
    C = 29 <= x <= 100
    f = D <= (((not C) and (not A)) <= (not D))
    if f != f_usl:
        print(x)
