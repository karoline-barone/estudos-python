'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''
from ex109 import moeda

valor = float(input('Digite um valor: R$ '))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumentando 15% temos {moeda.aumentar(valor, 15, True)}')
print(f'Diminuindo 8% temos {moeda.diminuir(valor, 8, True)}')
