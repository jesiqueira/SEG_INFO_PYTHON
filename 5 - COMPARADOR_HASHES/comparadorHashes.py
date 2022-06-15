import hashlib

arquivo_1 = 'a.txt'
arquivo_2 = 'b.txt'

hash_1 = hashlib.new('ripemd160')

hash_1.update(open(arquivo_1, 'rb').read()) #comparar o hashers

hash_2 = hashlib.new('ripemd160')

hash_2.update(open(arquivo_2, 'rb').read())

#comparar os arquivo

if hash_1.digest() != hash_2.digest():
    print(f'O arquivo: {arquivo_1} é diferente do arquivo: {arquivo_2}')
    print('O hash do arquivo a.txt é: ', hash_1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash_2.hexdigest())
else:
    print(f'O arquivo: {arquivo_1} é igual do arquivo: {arquivo_2}')
    print('O hash do arquivo b.txt é: ', hash_2.hexdigest()) 
    print('O hash do arquivo b.txt é: ', hash_2.hexdigest()) 
    print('O hash do arquivo a.txt é: ', hash_1.hexdigest())
    print('O hash do arquivo b.txt é: ', hash_2.hexdigest())