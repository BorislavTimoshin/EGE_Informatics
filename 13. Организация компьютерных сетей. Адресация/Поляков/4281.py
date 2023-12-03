for A in range(1, 1000):
    for x in range(100):
        for y in range(100):
            if (25 * x + 8 * y != 10000) or ((A > x) and A > y):
                pass
            else:
                break
        else:
            break
    else:
        pass
