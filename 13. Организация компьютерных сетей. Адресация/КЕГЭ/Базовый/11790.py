from ipaddress import ip_network

for A in range(256):
    try:
        net = ip_network(f"152.65.245.132/255.255.{A}.0", False)
        for ip in net:
            b = bin(int(ip))[2:]
            if b[:16].count("0") < b[16:].count("0"):
                break
        else:
            print(A)
            exit()
    except ValueError:
        pass
