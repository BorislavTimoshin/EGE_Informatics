from itertools import product
from re import search

counter = 0
for i in product("01234567", repeat=5):
    s = "".join(i)
    if s.count("6") == 1 and s[0] != "0" and search("[1357]6|6[1357]|[1357]6[1357]", s) is None:
        counter += 1
print(counter)
