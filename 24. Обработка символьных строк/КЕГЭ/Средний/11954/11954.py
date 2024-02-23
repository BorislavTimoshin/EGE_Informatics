# with open("24_11954.txt", "r", encoding="utf-8") as file:
#     text = file.read()
#     minim = 1e10
#     kx = 1
#     r = text.index("X")
#     l = text.index("X")
#     while r < len(text):
#         while kx != 500:
#             r += 1
#             if r == len(text):
#                 break
#             if text[r] == "X":
#                 kx += 1
#             if text[r] == "Y":
#                 l = r
#                 kx = 0
#                 while text[r] != "X":
#                     r += 1
#                     l += 1
#                     if r == len(text):
#                         print(minim)
#                         exit()
#                 if text[r] == "X":
#                     kx += 1
#         if kx == 500:
#             minim = min(minim, r - l + 1)
#             l += 1
#             kx -= 1
#         while text[l] != "X":
#             l += 1
#     print(minim)


with open("24_11954.txt", "r", encoding="utf-8") as file:
    text = file.read()
    kx = 0
    l = 0
    minim = 1e10
    for r in range(len(text)):
        if text[r] == "Y":
            l = r + 1
            kx = 0
        if text[r] == "X":
            kx += 1
        # Находим индекс следующего X с начала
        while kx == 500:
            minim = min(minim, r - l + 1)
            if text[l] == "X":
                kx -= 1
            l += 1
    print(minim)

