'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
numeros = []
cont = 0
while True:
    numeros.append(int(input('Digite um valor: ')))
    cont+=1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram digitados {cont} valores na lista.')
numeros.sort(reverse=True)
print(f'Lista de valores em forma decrescente: {numeros}')
if 5 in numeros:
    print('O valor 5 foi digitado na lista.')
else:
    print('O valor 5 não foi digitado na lista.')
