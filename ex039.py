'''Faca um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade se ele ainda vai se
alistar ao servico militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá
mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
anonasc = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonasc
if idade == 18:
    print(f'Quem nasceu em {anonasc} tem {idade} anos em {anoatual}.\n'
          f'Voce tem que se alistar imediatamente.')
elif idade < 18:
    print(f'Quem nasceu em {anonasc} tem {idade} anos em {anoatual}.\n'
          f'Ainda faltam {18 - idade} anos para o alistamento.\n'
          f'Seu alistamento será em {anoatual + (18 - idade)}.')
else:
    print(f'Quem nasceu em {anonasc} tem {idade} anos em {anoatual}.\n'
          f'Voce já deveria ter se alistado há {idade - 18} anos.\n'
          f'Seu alistamento foi em {anoatual - (idade - 18)}.')