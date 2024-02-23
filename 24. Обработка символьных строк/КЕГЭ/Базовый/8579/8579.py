from re import findall

with open("24_8579.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:[13579]\D*[24680])|(?:[24680]\D*[13579])", text)
    print(len(max(sequences, key=len)))

