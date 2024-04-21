for A in range(1000, -1, -1):
    for x in range(500):
        for y in range(500):
            if (3 * x + y > 48) or (x > y) or (4 * x + y < A):
                pass
            else:
                print(A)
                exit()
