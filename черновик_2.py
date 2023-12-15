# def f(x, p):
#     if x >= 429:
#         if p == 2:
#             return True
#         return False
#     else:
#         if p % 2 == 0:
#             return f(x + 5, p + 1) and f(x * 5, p + 1)
#         else:
#             return f(x + 5, p + 1) or f(x * 5, p + 1)
#
#
# for i in range(1, 428):
#     if f(i, 0):
#         print(i)
#         break

# def f(x, p):
#     if x >= 429:
#         if p == 3:
#             return True
#         return False
#     else:
#         if p % 2 == 1:
#             return f(x + 5, p + 1) and f(x * 5, p + 1)
#         else:
#             return f(x + 5, p + 1) or f(x * 5, p + 1)
#
#
# for i in range(1, 428):
#     if f(i, 0):
#         print(i)

# def f(x, p):
#     if x >= 429:
#         if p == 2 or p == 4:
#             return True
#         return False
#     else:
#         if p % 2 == 0:
#             return f(x + 5, p + 1) and f(x * 5, p + 1)
#         else:
#             return f(x + 5, p + 1) or f(x * 5, p + 1)
#
#
# for i in range(1, 428):
#     if f(i, 0):
#         print(i)
#         break

""" 11281 КЕГЭ """


def f(s, m):
    if s >= 429:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [f(s + 5, m - 1), f(s * 5, m - 1)]
    return any(h) if m % 2 != 0 else all(h)


print(19, min(s for s in range(1, 429) if f(s, 2)))
print(20, [s for s in range(1, 429) if not f(s, 1) and f(s, 3)][:2])
print(21, min(s for s in range(1, 429) if not f(s, 2) and f(s, 4)))
