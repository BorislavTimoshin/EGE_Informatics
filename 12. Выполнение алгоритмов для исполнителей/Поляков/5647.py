for k in range(200, 99, -1):
    for m in range(200, 99, -1):
        for n in range(200, 99, -1):
            s = ">" + m * "1" + n * "2" + k * "0"
            while ">1" in s or ">2" in s or ">0" in s:
                s = s.replace(">1", "20>", 1)
                s = s.replace(">2", "00>", 1)
                s = s.replace(">0", "10>", 1)
            if sum(map(int, s.replace(">", "", 1))) == 599:
                print(k)
