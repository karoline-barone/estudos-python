'''Desafio 023 - Implemente o diagrama de classes: Poligono (abstract) com qtd_lados, perimetro() abstract,e area() abstract.
Quadrado com lado, perimetro() e area(). E Circulo com raio, perimetro() e area() . Com simbologia de herança.'''
from poligonos import *

def main():
    poligono1 = Quadrado(12)
    poligono2 = Circulo(6)
    print(f'Um quadrado de lado {poligono1.lado} tem perimetro: {poligono1.perimetro()} e area {poligono1.area()}')
    print(f'Um circulo de raio {poligono2.raio} tem perimetro {poligono2.perimetro()} e area {poligono2.area()} ')

if __name__ == '__main__':
    main()