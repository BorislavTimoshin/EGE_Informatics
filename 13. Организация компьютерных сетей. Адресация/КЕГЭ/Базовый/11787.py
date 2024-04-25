from ipaddress import ip_network

net = ip_network(f"101.157.240.0/255.255.252.0", False)
counter = 0
for ip in net:
    b = bin(int(ip))[2:].zfill(32)
    if b[:16].count("1") > b[16:].count("1"):
        counter += 1
print(counter)
