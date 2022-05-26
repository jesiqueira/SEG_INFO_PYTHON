import socket
import sys  # fornece acesso a variaveis com interpretador python


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('Erro ao abrir conexão!!')
        print(f'Erro: {e}')
        sys.exit()

    print('Socket criado com sucesso.')

    hostAlvo = input('Digite o Host ou IP a ser conectado: ')
    portAlvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((hostAlvo, int(portAlvo)))
        print(
            f'Cliente tcp conectado com sucesso no host: {hostAlvo} na porta: {portAlvo}')
        s.shutdown(2)
    except socket.error as e:
        print(f'Erro ao conectar ao host: {hostAlvo} na porta: {portAlvo}')
        print(f'Error: {e}')
        sys.exit()


if __name__ == "__main__":
    main()