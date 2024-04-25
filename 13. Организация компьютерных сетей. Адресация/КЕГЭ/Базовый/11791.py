from ipaddress import ip_network

for A in range(256):
    try:
        net = ip_network(f"246.51.128.202/255.255.{A}.0", False)
        for ip in net:
            b = bin(int(ip))[2:].zfill(32)
            if b[:16].count("0") > b[16:].count("0"):
                break
        else:
            print(A)
            exit()
    except ValueError:
        pass
