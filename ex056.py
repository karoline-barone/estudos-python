'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos'''
somaidade = 0
maior = 0
nomemaior = ''
menor = 0
for c in range(1, 5):
    print(f'------ {c}ªpessoa ------')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    somaidade += idade
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    if sexo == 'M':
        if idade > maior:
            maior = idade
            nomemaior = nome
    if sexo == 'F' and idade < 20:
        menor += 1
print(f'A média de idade do grupo é de {somaidade/4} anos.')
print(f'O nome do homem mais velho é {nomemaior} e ele tem {maior} anos.')
print(f'{menor} mulheres com menos de 20 anos.')
