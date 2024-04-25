from ipaddress import ip_network

net = ip_network("192.168.32.128/255.255.255.192", False)
counter = 0
for ip in net:
    b = bin(int(ip))[2:].zfill(32)
    if b.count("1") % 2 == 0:
        counter += 1
print(counter)
