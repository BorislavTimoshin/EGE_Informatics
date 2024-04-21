ok = False
for A in range(1000):
    for x in range(500):
        if ok:
            ok = False
            break
        for y in range(500):
            if (x > 56) or (y >= x) or (3 * x - y < A):
                pass
            else:
                ok = True
                break
    else:
        print(A)
        break


# Или


def f(x, y):
    return (x > 56) or (y >= x) or (3 * x - y < A)


for A in range(1000):
    if all(f(x, y) for x in range(500) for y in range(500)):
        print(A)
        break
