#jo-ken-po com números

import random

print('Bem-Vindo')
input('Pressione Enter para começar')
while True:
    inp = input('Deseja jogar de 5, 10 ou 100? ')
    if inp == '5':
        sua = int(input('Digite um número'))
        rand = random.randint(1, 5)
        if sua == rand:
            print('Números iguais')
            print(f'{sua}, {rand}')
        else:
            print('Números diferentes')
            print(f'{sua}, {rand}')
    elif inp == '10':
        sua = int(input('Digite um número'))
        rand = random.randint(1, 10)
        if sua == rand:
            print('Números iguais')
            print(f'{sua}, {rand}')
        else:
            print('Números diferentes')
            print(f'{sua}, {rand}')
    elif inp == '100':
        sua = int(input('Digite um número'))
        rand = random.randint(1, 100)
        if sua == rand:
            print('Números iguais')
            print(f'{sua}, {rand}')
        else:
            print('Números diferentes')
            print(f'{sua}, {rand}')
