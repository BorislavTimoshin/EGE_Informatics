f = open(r"C:\Python_Projects\ЕГЭ\Задача 27\27889_РешуЕГЭ\27-B_demo.txt")
s = f.readlines()
n = int(s[0])
difference = 10 ** 4
summa = 0

for i in range(1, n + 1):
    x, y = map(int, s[i].split())
    summa += min(x, y)
    if abs(x - y) % 3 != 0:
        difference = min(difference, abs(x - y))

if summa % 3 != 0:
    print(summa)
else:
    print(summa - difference)
