'''Desafio024 - Simule uma cafeteria orientada a objetos, contendo:
- BebidaQuente (abstract) = preparar(), ferver_agua(), misturar() {abstract}, servir() {abstract}
- Cafe = misturar(), servir()
- Cha = misturar(), servir()
- Leite = misturar(), servir()'''
import cafeteria

def main():
    bebida1 = cafeteria.Cafe()
    bebida2 = cafeteria.Cha()
    bebida3 = cafeteria.Leite()
    bebida1.preparar()
    bebida2.preparar()
    bebida3.preparar()

if __name__ == '__main__':
    main()