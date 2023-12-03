minim = 1000000
for x in range(13):
    for y in range(13):
        M = int(f"2{y}23{x}5", 15)
        N = int(f"67{x}9{y}", 13)
        for A in range(1, 10000):
            if (M + A) % N == 0:
                if A < minim:
                    minim = A
print(minim)
