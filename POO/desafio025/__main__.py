'''Desafio025 - Crie classes capazes de calcular fretes de veículos diferentes:
- Transporte(abstract) = distancia(), frete(), calc_frete() {abstract}
- Moto = fator = 0.50, calc_frete(), limite livre
- Caminhao = fator = 1.20, calc_frete(), limite min 50 km
- Drone = fator = 9.50, calc_frete(), limite max 10 km'''
from transportes import *

def main():
    distancia = 5
    entrega = Drone(distancia)
    print(f'Frete de {type(entrega).__name__} de {distancia}km = {entrega.calc_frete()}')


if __name__ == '__main__':
    main()