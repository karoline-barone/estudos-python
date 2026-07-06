''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) Qual é o total gasto na compra
b) Quantos produtos custam mais de R$1000
c) Qual é o nome do produto mais barato '''
total = maisdemil = maisbarato = 0
nomemaisbarato = ' '
while True:
    print('Cadastro de produto')
    produto = str(input('Nome do produto: '))
    preco = int(input('Preço do produto: '))
    total += preco
    if preco > 1000:
        maisdemil += 1
    if maisbarato == 0 or preco < maisbarato:
        maisbarato = preco
        nomemaisbarato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total gasto na compra foi R${total}.')
print(f'{maisdemil} produtos custam mais de R$1000.')
print(f'O produto mais barato foi o {nomemaisbarato} e custou R${maisbarato}.')
