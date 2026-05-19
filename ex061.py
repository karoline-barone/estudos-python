# refazer o ex051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos de progressao usando a estrutura while
primeirotermo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
progressao = 0
while progressao < 10:
    print(primeirotermo + (razao*progressao), end=' -> ')
    progressao += 1
print('FIM')