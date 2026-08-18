'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa
tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
def maior(* num):
    cont = maior = 0
    print('-' * 30)
    print('Os valores informados foram:')
    for valor in num:
        sleep(0.5)
        print(f'{valor} ', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'\nForam informados {cont} números.')
    print(f'O maior número foi {maior}.')


maior(2, 9, 4, 7, 5, 6)
maior(3, 1, 4)
maior(6)
maior()
