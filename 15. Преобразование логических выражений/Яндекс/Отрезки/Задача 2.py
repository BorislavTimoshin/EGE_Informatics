# https://education.yandex.ru/ege/task/65d0889c-049f-4d09-8121-e39f155c96c3

A = range(15, 28)
B = range(10, 24)
C = range(12, 31)


def f(x):
    return (((x in B) <= (x in A)) <= (x in C))


print(f(22))
print(f(14))
print(f(43))
