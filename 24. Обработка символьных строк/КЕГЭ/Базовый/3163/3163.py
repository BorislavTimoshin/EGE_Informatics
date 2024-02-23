with open("24_3163.txt", "r", encoding="utf-8") as file:
    text = file.read()
    text1 = text.replace("PR", "P R").split()
    g = max(text1, key=len)
    text2 = text.replace("ST", "S T").split()
    h = max(text2, key=len)
    print(max(len(g), len(h)))
