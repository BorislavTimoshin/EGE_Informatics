with open(r"C:\Python_Projects\ЕГЭ_Информатика\27. Программирование\Поляков\6891\27-179b.txt", "r",
          encoding="utf-8") as file:
    N, *numbers = file.readlines()

N = int(N)
numbers = list(map(lambda x: list(map(int, x.split())), numbers))
first = [numbers[0][0]]
second = [numbers[0][1]]
counter = 1


def binary_search(number, lst):
    start = 0
    end = len(lst)
    while start < end:
        mid = (start + end) // 2
        if lst[mid] < number:
            start = mid + 1
        else:
            end = mid
    return start


for f, s in numbers[1:]:
    index = binary_search(f, first)
    if index == 0:
        if s <= first[0]:
            counter += 1
            first.insert(index, f)
            second.insert(index, s)
    elif index == len(first) or (len(first) == 1 and index == 1):
        if f >= second[-1]:
            counter += 1
            first.insert(index, f)
            second.insert(index, s)
    elif f >= second[index - 1] and s <= first[index]:
        counter += 1
        first.insert(index, f)
        second.insert(index, s)

print(counter)
