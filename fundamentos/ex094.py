'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
pessoa = {}
todos = []
mulheres = []
acimamedia = []
cont = 0
soma = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    cont += 1
    soma += pessoa['idade']
    todos.append(pessoa.copy())
    pessoa.clear()
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print(f'A)Foram cadastradas {cont} pessoas.')
print(f'B)A média de idade foi {(soma / cont):.2f} anos.')
print(f'C)As mulheres cadastradas foram {mulheres}')
print(f'D)Pessoas com idade acima da media:')
for pessoa in todos:
    if pessoa['idade'] > soma / cont:
        print('    ')
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
