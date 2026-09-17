'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from ex107 import moeda

valor = float(input('Digite um valor: R$ '))
print(f'A metade de R${valor} é R${moeda.metade(valor)}')
print(f'O dobro de R${valor} é R${moeda.dobro(valor)}')
print(f'Aumentando 15% temos R${moeda.aumentar(valor, 15)}')
print(f'Diminuindo 8% temos R${moeda.diminuir(valor, 8)}')
