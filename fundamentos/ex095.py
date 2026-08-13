'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador.'''
jogador = {}
todos = []
while True:
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? : '))
    jogador['gols'] = []
    soma = 0
    for i in range(0, partidas):
        qtdd = int(input(f'Quantos gols na partida {i+1}? '))
        jogador['gols'].append(qtdd)
        soma += qtdd
    jogador['total'] = soma
    todos.append(jogador.copy())
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Cadastrar outro jogador? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-='*20)
print(f'{"cod":<4}{"nome":<15}{"gols":<20}{"total":<5}')
print('-'*40)
for i, j in enumerate(todos):
    print(f'{i:<4}{j["nome"]:<15}{str(j["gols"]):<20}{j["total"]:<5}')
print('-'*30)
while True:
    dados = int(input(f'Mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        break
    if dados >= len(todos):
        print('Erro. Número de jogador inexistente. Tente novamente.')
        continue
    else:
        print(f'Dados do jogador {todos[dados]["nome"]}:')
        for i, v in enumerate(todos[dados]['gols']):
            print(f'=> Na partida {i+1} fez {v} gols.')
