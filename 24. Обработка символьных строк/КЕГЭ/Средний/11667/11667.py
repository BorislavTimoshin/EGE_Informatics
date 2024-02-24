# with open("24_11667.txt", "r", encoding="utf-8") as file:
#     text = file.read()
#     k = 0
#     l = 0
#     maxim = 0
#     for i in range(7, len(text)):
#         if text[i-7:i+1] == "INFINITY":
#             k += 1
#         while k == 1001:
#             if text[l:l+8] == "INFINITY":
#                 k -= 1
#             l += 1
#         if k == 1000:
#             maxim = max(maxim, i - l + 1)
#     print(maxim)

# Или

with open("24_11667.txt", "r", encoding="utf-8") as file:
    text = file.read()
    CONST = 1000
    inds = [0] + [i for i in range(len(text) - 7) if text[i:i+8] == "INFINITY"] + [len(text)]
    lenght = len(inds) - CONST
    inds = [0] + inds + [len(text)]
    maxim = 0
    for i in range(1, lenght):
        indexes = inds[i-1:i+1001]
        if len(indexes) == 1002:
            answer = indexes[-1] - indexes[0] - 1
            if answer > maxim:
                maxim = answer
    print(maxim + 7)  # Прибавляем 7, так мы не учли, что не были добавлены 7 символов INFINIT от последнего INFINITY
