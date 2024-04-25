# https://education.yandex.ru/ege/task/e0a69d93-9830-45fb-981a-804016be561a

from ipaddress import ip_network, ip_address

for mask in range(1, 33):
    net = ip_network(f"134.181.67.112/{mask}", False)
    if ip_address("134.181.67.112") in net and ip_address("134.181.94.117") in net:
        print(mask, net.netmask)
# Ответ 255 + 224 = 479
