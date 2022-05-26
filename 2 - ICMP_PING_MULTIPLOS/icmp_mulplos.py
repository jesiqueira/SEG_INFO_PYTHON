from ast import dump
import os
import time
with open('host.txt') as file:
    dumps = file.readlines()

    for ip in dumps:
        os.system(f'ping -n 2 {ip}')
        time.sleep(3)
