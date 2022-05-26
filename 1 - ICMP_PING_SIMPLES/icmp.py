import os

print('#' * 60)
ip_ou_host = input("Digite IP ou Host a ser Verificado: ")

os.system(f'ping -n 6 {ip_ou_host} ')
print('#' * 60)
