import csv
from re import split


def rec(identifier):
    if dict1[identifier] == [0]:
        return dict2[identifier]
    return dict2[identifier] + max(rec(i) for i in dict1[identifier])


with open(r"C:\Python_Projects\ЕГЭ_Информатика\22. Многопроцессорные системы\Поляков\6499\file.csv", "r",
          encoding="utf-8") as file:
    # Построение стандартной таблицы процессов (без смещения независимыз процессов). Пример:
    # C:\Python_Projects\ЕГЭ_Информатика\22. Многопроцессорные системы\Поляков\6524\6524.xls
    reader = list(csv.reader(file, delimiter=";"))[1:]
    dict1 = dict()
    dict2 = dict()
    matrix = [[0] * 400 for i in range(len(reader))]
    for row in reader:
        id_B = int(row[0])
        execution_time = int(row[1])
        idsA = split(r"\D+", row[2])
        dict1[id_B] = list(map(int, idsA))
        dict2[id_B] = execution_time
    for i, key in enumerate(dict1):
        his_time = dict2[key]
        maxim_process_time = rec(key) - his_time
        for j in range(maxim_process_time, maxim_process_time + his_time):
            matrix[i][j] = 1
    new_matrix = list(zip(*matrix))
    column_100 = new_matrix[99]
    print(sum(column_100))
