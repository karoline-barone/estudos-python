'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''
pessoa = []
grupo = []
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(grupo) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa [1] > maior:
            maior = pessoa [1]
        if pessoa [1] < menor:
            menor = pessoa [1]
    grupo.append(pessoa[:])
    pessoa.clear()
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(grupo)} pessoas.')
print(f'O maior peso foi de {maior} kg. Pessoa(s) com esse peso:', end = ' ')
for p in grupo:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso foi de {menor} kg. Pessoa(s) com esse peso:', end = ' ')
for p in grupo:
    if p[1] == menor:
        print(p[0], end =' ')
