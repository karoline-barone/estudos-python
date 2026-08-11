'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input("Digite o nome: "))
anonasc = int(input("Digite o ano de nascimento: "))
pessoa['idade'] = datetime.now().year - anonasc
pessoa['ctps'] = int(input("Digite o ctps (0 não tem): "))
if pessoa['ctps'] != 0:
    pessoa['anocont'] = int(input("Digite o ano de contratação: "))
    pessoa['salario'] = float(input("Digite o salário: "))
    pessoa['aposentadoria'] = (pessoa['anocont'] + 35) - anonasc
for k, v in pessoa.items():
    print(f'{k} = {v}')
