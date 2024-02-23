import os

# Пути задач, которые пока не получилось решить
unresolved_tasks = [
    r"C:\Python_Projects\ЕГЭ_Информатика\27. Программирование\Поляков\6868\6868.py",
    r"C:\Python_Projects\ЕГЭ_Информатика\24. Обработка символьных строк\КЕГЭ\Базовый"
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

""" Проверка на то, решался ли введенный номер ЕГЭ """

website = input()  # Решу ЕГЭ, Поляков, КЕГЭ
number_of_task = int(input())

if number_of_task in task_1:
    print("Файл существует - 1. Анализ информационных моделей")
    exit()
if number_of_task in task_1:
    print("Файл существует - 4. Кодирование и декодирование информации")
    exit()
if number_of_task in task_1:
    print("Файл существует - 7. Кодирование и декодирование информации. Передача информации")
    exit()
if number_of_task in task_1:
    print("Файл существует - 11. Вычисление количества информации")
    exit()

main_directory = os.getcwd()
flag = True

for currentdir, dirs, files in os.walk(main_directory):
    if website in currentdir:
        for file in files:
            if file.startswith(str(number_of_task)):
                print(fr"Файл существует - {currentdir}\{file}")
                flag = False
if flag:
    print("Файл не существует")
