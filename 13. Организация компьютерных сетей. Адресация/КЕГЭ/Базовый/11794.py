from ipaddress import ip_network

for A in range(255, 0, -1):
    net = ip_network(f"223.167.{A}.167/255.255.255.192", False)
    for ip in net:
        b = bin(int(ip))[2:].zfill(32)
        if b[:16].count("0") > b[16:].count("0"):
            break
    else:
        print(A)
        break
