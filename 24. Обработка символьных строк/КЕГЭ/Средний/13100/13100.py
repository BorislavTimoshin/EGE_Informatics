# with open("24_13100.txt", "r", encoding="utf-8") as file:
#     text = file.read()
#     indexes = [(i, s) for i, s in enumerate(text) if s == "C" or s == "D"]
#     maxim = 0
#     for i in range(len(indexes)):
#         lst = indexes[i:i+4]
#         lst2 = list(map(lambda x: x[1], lst))
#         if lst2.count("C") == 2 and lst2.count("D") == 2:
#             last_index = indexes[i - 1][0]
#             future_index = indexes[i + 4][0]
#             answer = (lst[0][0] - last_index) + (future_index - lst[3][0]) + (lst[3][0] - lst[0][0] - 1)
#             if answer > maxim:
#                 maxim = answer
#     print(maxim)


with open("24_13100.txt", "r", encoding="utf-8") as file:
    text = file.read()
    kc = 0
    kd = 0

    l = 0
    r = 0

    maxim = 0

    while r < len(text):
        while kc <= 2 and kd <= 2:
            maxim = max(maxim, r - l + 1)
            r += 1
            if r == len(text):
                break
            if text[r] == "C":
                kc += 1
            if text[r] == "D":
                kd += 1
        while not (kc <= 2 and kd <= 2):
            if text[l] == "C":
                kc -= 1
            if text[l] == "D":
                kd -= 1
            l += 1
    maxim = max(maxim, r - l + 1)
    print(maxim)
