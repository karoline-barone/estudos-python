'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
numeros = []
while True:
    novonumero = int(input('Digite um valor: '))
    numeros.append(novonumero)
    for i in range(len(numeros)-1):
        if numeros[i] == novonumero:
            print('Esse número já foi digitado. Tente novamente.')
            numeros.pop()
            continue
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
numeros.sort()
print(f'Os valores digitados foram {numeros}')
