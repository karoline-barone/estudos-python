#leia um número qualquer e mostre o seu fatorial
num = int(input('Digite um número inteiro: '))
c = num
fatorial = 1
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    fatorial *= c
    c -= 1
print(f'{fatorial}')
print(f'O fatorial de {num} é {fatorial}.')