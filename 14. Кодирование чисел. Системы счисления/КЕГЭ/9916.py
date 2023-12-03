from collections import Counter

number = 5 * 3 ** 1917 + 6 * 2 ** 1878 + 7 * 3 ** 1870 - 1991
lst = []

while number > 0:
    value = number % 17
    lst.append(value)
    number //= 17

print(Counter(lst))
