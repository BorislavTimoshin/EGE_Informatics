P = range(56, 80)
Q = range(63, 86)


def f(x, a):
    return (not ((x in P) <= (x in Q))) <= (not (x in Q) <= (x in a))

