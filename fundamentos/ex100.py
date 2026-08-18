'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares
sorteados pela função anterior.'''
from random import randint
def sorteia():
    numeros = [randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)]
    print(f'Os números sorteados foram: {numeros}')
    return numeros
def somaPar():
    soma = 0
    for n in valores:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {valores} temos {soma}')


valores = sorteia()
somaPar()


