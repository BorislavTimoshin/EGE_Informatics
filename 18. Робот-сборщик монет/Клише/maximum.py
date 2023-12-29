path = r"C:\Python_Projects\ЕГЭ_Информатика\18. Робот-сборщик монет\Клише\example.txt"
with open(path, "r", encoding="utf-8") as file:
    numbers = [list(map(int, i.split())) for i in file.read().split("\n")]

len_x = len(numbers[0]) - 1
len_y = len(numbers) - 1
p = 1
for i in range(len_x - 1, -1, -1):
    numbers[len_y][i] += numbers[len_y][i + 1]
for i in range(len_y - 1, -1, -1):
    numbers[i][len_x] += numbers[i + 1][len_x]
len_x -= 1
len_y -= 1
while len_x >= 0 and len_y >= 0:
    for i in range(len_x, -1, -1):
        numbers[len_y][i] += max(numbers[len_y + 1][i], numbers[len_y][i + 1])
    for j in range(len_y - 1, -1, -1):
        numbers[j][len_x] += max(numbers[j + 1][len_x], numbers[j][len_x + 1])
    len_y -= 1
    len_x -= 1

print(numbers[0][0])
