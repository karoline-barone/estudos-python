''' Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''
from time import sleep
def contador(inicio, fim, passo):
    print('-'*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            sleep(0.5)
            print(i, end=' ')
    else:
        passo = -passo
        for i in range(inicio, fim - 1, passo):
            sleep(0.5)
            print(i, end=' ')
    print('FIM!')
    print('-'*30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
