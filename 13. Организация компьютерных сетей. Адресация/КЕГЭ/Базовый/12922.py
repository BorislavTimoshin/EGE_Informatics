from ipaddress import ip_network

net = ip_network("136.36.240.16/255.255.255.248", False)
counter = 0

for ip in net:
    b = bin(int(ip))[2:]
    if "101" not in b:
        counter += 1
print(counter)
