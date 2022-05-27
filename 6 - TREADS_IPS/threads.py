from threading import Thread
import time


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(1)
        print(f'\nVelocidade: {trajeto}, Piloto: {piloto}')

th_carro_1 = Thread(target=carro, args=[1, 'Edmar'])
th_carro_2 = Thread(target=carro, args=[1.5, 'Lucas'])

th_carro_1.start()
th_carro_2.start()