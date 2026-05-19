#melhore o ex061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos
primeirotermo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
progressao = 0
total = 0
termos = 10
while termos != 0:
    total += termos
    while progressao < total:
        print(primeirotermo + (razao*progressao), end=' -> ')
        progressao += 1
    print('PAUSA')
    termos = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
