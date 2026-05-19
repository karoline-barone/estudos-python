#refaca o desafio 009 mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laco for.
num = int(input('Digite um número inteiro para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{num} X {c:2} = {num*c}')