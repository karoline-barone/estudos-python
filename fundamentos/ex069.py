'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
a) Quantas pessoas tem mais de 18 anos
b) Quantos homens cadastrados
c) Quantos mulheres tem menos de 20 anos'''
maior = homens = mulheres = 0
while True:
    print('Cadastre uma pessoa:')
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'{maior} pessoas tem mais de 18 anos.')
print(f'{homens} homens cadastrados.')
print(f'{mulheres} mulheres com menos de 20 anos.')
