def f(x, p):
    if x >= 429:
        if p == 2:
            return True
        return False
    else:
        if p % 2 == 0:
            return f(x + 5, p + 1) and f(x * 5, p + 1)
        else:
            return f(x + 5, p + 1) or f(x * 5, p + 1)


for i in range(1, 428):
    if f(i, 0):
        print(i)
        break
