from ipaddress import ip_network

for A in range(256):
    try:
        net = ip_network(f"99.8.254.232/255.255.{A}.0", False)
        for ip in net:
            b = bin(int(ip))[2:]
            if A == 248:
                print(b[:16].count("1") > b[16:].count("1"))
        #     if b[:16].count("1") > b[16:].count("1"):
        #         break
        # else:
        #     print(A)
        #     break
    except ValueError:
        pass
