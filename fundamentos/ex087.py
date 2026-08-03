'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somatc = maiorsl = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if matriz[l][2]:
            somatc += matriz[l][2]
        if matriz[1][c]:
            if matriz[1][0]:
                maiorsl = matriz[1][0]
            if matriz[1][c] > maiorsl:
                    maiorsl = matriz[1][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares digitados é {somapar}.')
print(f'A soma dos valores da terceira coluna é {somatc}.')
print(f'O maior valor da segunda linha é {maiorsl}.')
