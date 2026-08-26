'''Desafio021 - Crie a classe caneta, que simule o funcionamento de uma caneta colorida, podendo escrever frases na cor relativa'''
class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampada = True

    def tampar(self):
        self.tampada = True

    def destampar(self):
        self.tampada = False

    def escrever(self, frase):
        if self.tampada:
            print(f"A caneta {self.cor} está tampada")
        else:
            if self.cor == "azul":
                print(f'\033[34m{frase}\033[0m', end='')
            elif self.cor == "vermelha":
                print(f'\033[31m{frase}\033[0m', end='')
            elif self.cor == "verde":
                print(f'\033[32m{frase}\033[0m', end='')
            else:
                print(f'{frase}', end = '')

    def quebrar_linha(self, qtdd):
        print(f"\n"*qtdd, end = '')


c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, Mundo!")
c1.quebrar_linha(2)
c2.escrever("Funciona!")
c3.escrever("Deu certo!")

c3.tampar()
c3.quebrar_linha(1)
c3.escrever("E agora?")
