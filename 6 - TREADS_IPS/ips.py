import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)
print('Endereço IP:', endereco + 300)

ip_rede = '192.168.0.1/24'

rede = ipaddress.ip_network(ip_rede, strict=False)
for ip in rede:
    print(f'IP: {ip}')
    
print('Rede: ', rede)
