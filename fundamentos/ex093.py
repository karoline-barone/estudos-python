'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas
partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
dicionário, incluindo o total de gols feitos durante o campeonato.'''
jogador = {}
jogador['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? : '))
jogador['gols'] = []
soma = 0
for i in range(0, partidas):
    qtdd = int(input(f'Quantos gols na partida {i+1}? '))
    jogador['gols'].append(qtdd)
    soma += qtdd
jogador['total'] = soma
print('-='*15)
print(jogador)
print('-='*15)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*15)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'=> Na partida {i} fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print('-='*15)
