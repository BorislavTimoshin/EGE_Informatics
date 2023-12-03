minim = 1000000
for A in range(1, 10000):
    for X in range(1, 10000):
        if (X & 1097 == 0) <= ((X & 2047 != 0) <= (X & A != 0)):
            pass
        else:
            break
    else:
        print(A)
        exit()
