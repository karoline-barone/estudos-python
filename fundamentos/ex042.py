'''Refaca o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
- Equilátero: todos os lados iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados diferentes'''
s1 = float(input('Digite o valor do primeiro segmento: '))
s2 = float(input('Digite o valor do segundo segmento: '))
s3 = float(input('Digite o valor do terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um triangulo', end=' ')
    if s1 == s2 == s3:
        print('EQUILÁTERO.')
    elif s1 != s2 != s3 != s1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os segmentos acima não podem formar um triangulo.')
    