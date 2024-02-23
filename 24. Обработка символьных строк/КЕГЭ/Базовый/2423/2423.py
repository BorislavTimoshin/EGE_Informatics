from re import findall

with open("24_2423.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"0?1?2?3?4?5?6?7?8?9?", text)
    print(max(sequences, key=len))
    print(len(max(sequences, key=len)))
