'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from operator import itemgetter
from random import randint
from time import sleep
jogadores = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
ordem = {}
print('Valores sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ordem = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Ordem:')
for i, j in enumerate(ordem):
    print(f'O {i+1}° lugar foi {j[0]} com {j[1]}.')
    sleep(1)
