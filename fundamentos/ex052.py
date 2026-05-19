#faca um programa que leia um numero inteiro e diga se ele é ou nao um numero primo
num = int(input('Digite um número: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print(f'\033[33m{c}', end=' ')
        cont += 1
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {cont} vezes.')
if cont == 2:
    print(f'O número {num} é PRIMO.')
else:
    print(f'O número {num} NÃO É PRIMO.')
