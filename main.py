import sys
import os
from re import fullmatch

# Пути задач, которые пока не получилось решить
unresolved_tasks = [
    r"C:\Python_Projects\ЕГЭ_Информатика\27. Программирование\Поляков\6868\6868.py",
    r"C:\\Python_Projects\\ЕГЭ_Информатика\\18. Робот-сборщик монет\\КЕГЭ\\Средний\\7040.py"
]

# Анализ информационных моделей
task_1 = [

]
# Кодирование и декодирование информации
task_4 = [

]
# Кодирование и декодирование информации. Передача информации
task_7 = [

]
# Вычисление количества информации
task_11 = [

]


def solution_exists():
    """ Проверка на то, существует ли решение введенного номера ЕГЭ """
    website = input()  # Решу ЕГЭ, Поляков, КЕГЭ
    number_of_task = int(input())  # Номер задания
    if number_of_task in task_1:
        print("Файл существует - 1. Анализ информационных моделей")
        sys.exit()
    if number_of_task in task_1:
        print("Файл существует - 4. Кодирование и декодирование информации")
        sys.exit()
    if number_of_task in task_1:
        print("Файл существует - 7. Кодирование и декодирование информации. Передача информации")
        sys.exit()
    if number_of_task in task_1:
        print("Файл существует - 11. Вычисление количества информации")
        sys.exit()

    main_directory = os.getcwd()
    flag = True
    for currentdir, dirs, files in os.walk(main_directory):
        if website in currentdir:
            for file in files:
                if fullmatch(fr".*{number_of_task}\..+", file):
                    print(fr"Файл существует - {currentdir}\{file}")
                    flag = False
    if flag:
        print("Файл не существует")


solution_exists()
