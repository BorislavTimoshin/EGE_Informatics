from itertools import product

counter = 0
for i in product("012345678", repeat=7):
    s = "".join(i)
    if s.count("6") == 1 and s[0] != "0" and (s.count("1") + s.count("3") + s.count("5") + s.count("7") + s.count("9")) == 2:
        counter += 1
print(counter)

""" Или """

counter = 0
for i in range(1_000_000, 8_888_889):
    s = str(i)
    if s.count("6") == 1 and (s.count("1") + s.count("3") + s.count("5") + s.count("7") + s.count("9")) == 2 and s.count("9") == 0:
        counter += 1
print(counter)
