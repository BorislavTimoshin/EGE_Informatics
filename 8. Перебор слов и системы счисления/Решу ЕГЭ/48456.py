from itertools import product

count = 0
for p in product("012345678", repeat=6):
    if p.count("4") == 1 and p[0] != "0" and (p.count("1") + p.count("3") + p.count("5") + p.count("7")) == 2:
        count += 1
print(count)

""" Или """

counter = 0
for i in range(100000, 888889):
    s = str(i)
    if s.count("4") == 1 and s.count("1") + s.count("3") + s.count("5") + s.count("7") + s.count("9") == 2 and s.count(
            "9") == 0:
        counter += 1
print(counter)
