from ipaddress import ip_network, ip_address

for mask in range(1, 33):
    net = ip_network(f"112.117.107.70/{mask}", False)
    if ip_address("112.117.107.70") in net and ip_address("112.117.121.80") in net:
        print(mask, net.netmask)

# Ответ 224
