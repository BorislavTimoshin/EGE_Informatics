from ipaddress import ip_network, IPv4Address

net = ip_network("192.168.32.128/255.255.255.192", False)
counter = 0
for i in net:
    s = bin(int(IPv4Address(i)))[2:]
    if s.count("1") % 2 == 0:
        counter += 1
print(counter)
