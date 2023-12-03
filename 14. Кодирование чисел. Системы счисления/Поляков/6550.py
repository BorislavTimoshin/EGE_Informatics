for p in range(2, 5000):
    for q in range(2, 5000):
        if str(p) == str(q)[::-1]:
            n1 = 1 * p ** 0 + 6 * p ** 1 + 9 * p ** 2
            n2 = 9 * q ** 0 + 6 * q ** 1 + 1 * q ** 2
            if n1 == n2:
                print(p)
