# https://education.yandex.ru/ege/task/5d4b5c19-3b39-4c8b-9127-a3b4fb59d49a
from ipaddress import ip_network

for mask in range(32, 0, -1):
    net = ip_network(f"192.168.1.0/{mask}", False)
    if len(list(net)) == 32:
        for ip in net:
            s = bin(int(ip))[2:][-8:]
            if s[-1] == "0" and s.count("1") == s.count("0"):
                print(s)
        exit()
