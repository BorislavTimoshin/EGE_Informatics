def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


minim = 1e10
for n1 in range(1, 100):
    for n2 in range(1, 100):
        if n1 + n2 >= 40:
            s = "0" + "1" * n1 + "2" * n2
            summa_a = sum(map(int, s))
            start_lenght = 1 + n1 + n2
            while "01" in s or "02" in s:
                s = s.replace("02", "1110", 1)
                s = s.replace("01", "220", 1)
            summa_s = sum(map(int, s))
            if is_prime(summa_s):
                if summa_a < minim:
                    minim = summa_a
print(minim)
