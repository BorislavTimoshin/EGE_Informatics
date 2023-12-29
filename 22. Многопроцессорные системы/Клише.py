d = {"0": 0}
path = ""
data = [s.replace(";", " ").split() for s in open(path)]

while len(d) != len(data) + 1:
    for s in data:
        if all(sub in d for sub in s[2:]):
            d[s[0]] = int(s[1]) + max(d[sub] for sub in s[2:])

print(max(d.values()))
