'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas
os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
valores = []
pares = []
impares = []
while True:
    novovalor = int(input('Digite um valor: '))
    valores.append(novovalor)
    if novovalor % 2 == 0:
        pares.append(novovalor)
    else:
        impares.append(novovalor)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N] ? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Lista de valores completa: {valores}')
print(f'Lista de pares: {pares}')
print(f'Lista de impares: {impares}')
