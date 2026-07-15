'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
times = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR', 'Bragantino', 'Bahia', 'Coritiba',
         'São Paulo', 'Atlético-MG', 'Corinthians', 'Cruzeiro', 'Botafogo', 'EC Vitória', 'Internacional',
         'Santos', 'Grêmio', 'Vasco da Gama', 'Remo', 'Mirassol', 'Chapecoense')
print(f'Lista de times 20 primeiros colocados do brasileirão: {times}')
print(f'Os cinco primeiros times são {times[0:5]}')
print(f'Os quatro últimos colocados: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'Posição do time da Chapecoense: {times.index("Chapecoense")+1}')
