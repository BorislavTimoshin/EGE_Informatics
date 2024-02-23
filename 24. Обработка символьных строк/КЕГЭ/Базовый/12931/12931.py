from re import findall

with open("24_12931.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:VWXYZ)+", text)
    print(len("VWXYZVWXYZVWXYZVWXYZVWXYZVWXYZVWXYZ") + 5)