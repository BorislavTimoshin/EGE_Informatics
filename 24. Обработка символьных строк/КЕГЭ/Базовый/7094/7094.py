from re import findall

with open("24_7094.txt", "r", encoding="utf-8") as file:
    text = file.read()
    sequences = findall(r"(?:[CDF][AU])+", text)
    print(sequences)
    print(len(max(sequences, key=len)) // 2)


