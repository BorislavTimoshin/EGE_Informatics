import csv

""" 9 номер ЕГЭ. Задача 2512 из КЕГЭ """

# Изначальный рейтинг детей

with open("Дети.csv", "r") as file_1:
    reader_1 = list(csv.reader(file_1))

    main_rating: dict[str, int] = dict()
    for info in reader_1[1:]:
        list_info_1 = "".join(info).split(";")
        main_rating[list_info_1[0]] = int(list_info_1[3])

# id пакости и рейтинг пакости

with open("Пакости.csv", "r") as file_2:
    reader_2 = list(csv.reader(file_2))

    bad_rating: dict[str, int] = dict()
    for info in reader_2[1:]:
        list_info_2 = "".join(info).split(";")
        bad_rating[list_info_2[0]] = int(list_info_2[2])

# Регистрация пакостей

with open("Регистрация пакостей.csv", "r") as file_3:
    reader_3 = list(csv.reader(file_3))

    for info in reader_3[1:]:
        list_info_3 = "".join(info).split(";")
        main_rating[list_info_3[0]] += bad_rating[list_info_3[1]]

# id доброго дела и рейтинг доброго дела

with open("Добрые дела.csv", "r") as file_4:
    reader_4 = list(csv.reader(file_4))

    good_rating: dict[str, int] = dict()
    for info in reader_4[1:]:
        list_info_4 = "".join(info).split(";")
        good_rating[list_info_4[0]] = int(list_info_4[2])

# Регистрация добрых дел

with open("Регистрация добрых дел.csv", "r") as file_5:
    reader_5 = list(csv.reader(file_5))

    for info in reader_5[1:]:
        list_info_5 = "".join(info).split(";")
        main_rating[list_info_5[0]] += good_rating[list_info_5[1]]

counter_mega = 0
counter_no_mega = 0
for id_child, rating in main_rating.items():
    if rating > 80:
        counter_mega += 1
    if rating > 0:
        counter_no_mega += 1

answer = counter_mega / counter_no_mega * 100
print(int(answer - answer % 1))
