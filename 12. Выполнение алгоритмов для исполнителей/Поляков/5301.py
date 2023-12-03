st = set()
for i in range(1, 1000):
    s = "1" * i
    while "1111" in s or "222" in s or "33" in s:
        if "1111" in s:
            s = s.replace("1111", "333", 1)
        else:
            if "222" in s:
                s = s.replace("222", "11", 1)
            else:
                s = s.replace("33", "2", 1)
    st.add(s)
print(len(st))
