from itertools import permutations


numerals = list(range(17))
primes = [2, 3, 5, 7, 11, 13]
counter = 0

for i in permutations(numerals, 6):
    for j in i:
        if j in primes:
            break
    else:
        if i[0] % 2 == 0 and i[0] != 0:
            counter += 1

print(counter)
