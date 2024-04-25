from ipaddress import ip_network

net = ip_network("192.168.32.48/255.255.255.240", False)
counter = 0

for ip in net:
    b = bin(int(ip))[2:]
    if b.count("1") % 2 == 1:
        counter += 1
print(counter)
