from itertools import accumulate


""" Поиск максимальной подпоследовательности в последовательности положительных чисел, замкнутой в кольцо, длиной не 
более n, сумма и количество элементов которой кратны 13 Номер 27 в ЕГЭ, номер 5879 на сайте Полякова """

file_1 = open(r"C:\Python_Projects\ЕГЭ\Задача 27\5879_Поляков\file_1.txt").read().split("\n")[:-1]
file_2 = open(r"C:\Python_Projects\ЕГЭ\Задача 27\5879_Поляков\file_2.txt").read().split("\n")[:-1]
n1 = int(file_1[0])
n2 = int(file_2[0])
list_numbers_1 = list(map(int, file_1))[1:] * 2
list_numbers_2 = list(map(int, file_2))[1:] * 2


def main(list_numbers: list[int], n: int) -> int:
    max_sum = 0
    sums_nums = list(accumulate(list_numbers))
    for first_ind in range(n):
        for other_ind in range(first_ind, first_ind + n, 13):
            summa = sums_nums[other_ind] - sums_nums[first_ind]
            if summa % 13 == 0:
                max_sum = max(max_sum, summa)
    return max_sum


print(main(list_numbers_1, n1))
print(main(list_numbers_2, n2))
