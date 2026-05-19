'''A Confederacao Nacional de Natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SENIOR
- Acima: MASTER'''
from datetime import date
anonasc = int(input('Digite o ano de nascimento do atleta: '))
anoatual = date.today().year
idade = anoatual - anonasc
if idade <= 9: print(f'O atleta tem {idade} anos. Está na categoria: MIRIM.')
elif idade <= 14: print(f'O atleta tem {idade} anos. Está na categoria: INFANTIL.')
elif idade <=19: print(f'O atleta tem {idade} anos. Está na categoria: JUNIOR.')
elif idade <=25: print(f'O atleta tem {idade} anos. Está na categoria: SENIOR')
else: print(f'O atleta tem {idade} anos. Está na categoria: MASTER')
