#crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda nao atingiram a maioridade e quantas já sao maiores.
from datetime import date
menor = 0
maior = 0
anoatual = date.today().year
for c in range(0, 7):
    anonasc = int(input(f'Qual o ano de nascimento da {c+1} pessoa? '))
    if anoatual - anonasc >= 18:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas maiores de 18 anos.')
print(f'{menor} pessoas menores de 18 anos.')