from itertools import accumulate

with open(r"C:\Python_Projects\ЕГЭ_Информатика\27. Программирование\Поляков\6868\27-178b.txt", "r",
          encoding="utf-8") as file:
    N, *numbers = map(int, file.readlines())

numbers *= 2
acc = accumulate(numbers)


def main(list_numbers: list[int], n: int) -> int:
    max_sum = 0
    sums_nums = list(accumulate(list_numbers))
    for first_ind in range(n):
        for other_ind in range(first_ind, first_ind + n):
            summa = sums_nums[other_ind] - sums_nums[first_ind]
            max_sum = max(max_sum, summa)
    return max_sum


print(main(numbers, N))


""" Не решил """
