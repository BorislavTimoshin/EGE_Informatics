for A in range(1000):
    flag = False
    for x in range(500):
        if flag:
            break
        for y in range(500):
            if (x ** 2 + y ** 2 > 1024 - x) or (y < -2 * x + A):
                pass
            else:
                flag = True
                break
    else:
        print(A)
        break
