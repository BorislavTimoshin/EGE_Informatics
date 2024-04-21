with open("6832.txt", "r", encoding="utf-8") as file:
    numbers = [list(map(int, i.split())) for i in file.read().split("\n")]

len_x = len(numbers[0])
len_y = len(numbers)
summs = []


def rec(y, x, summa):
    if y == len_y - 1 and x == len_x - 1:
        summs.append(summa + numbers[y][x])
        return
    elif x == 4 and y == 4:
        rec(y + 1, x, summa + numbers[y][x])
        rec(y, x + 1, summa + numbers[y][x])
    elif y == 4 and 5 <= x <= 13:
        rec(y, x + 1, summa + numbers[y][x])
    elif x == 4 and 5 <= y <= 13:
        rec(y + 1, x, summa + numbers[y][x])
    elif y == len_y - 1:
        rec(y, x + 1, summa + numbers[y][x])
    elif x == len_x - 1:
        rec(y + 1, x, summa + numbers[y][x])
    else:
        rec(y + 1, x, summa + numbers[y][x])
        rec(y, x + 1, summa + numbers[y][x])


rec(0, 0, 0)
print(max(summs))
print(min(summs))
