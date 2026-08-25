'''Desafio 018 - Crie uma classe chamada churrasco, onde seja possível informar quantas pessoas vão participar e mostre
quanto de carne deve ser comprado, o custo total do churrasco e o preço por pessoa.'''
class Churrasco:
    def __init__(self, nome = '', pessoas = 0):
        self.nome = nome
        self.pessoas = pessoas

    def __str__(self):
        qtddcarne = self.pessoas*0.4
        custototal = qtddcarne*82.40
        return (f"Analisando {self.nome} com {self.pessoas} convidados:\n"
                f"Cada participante comerá 0.4 kg de carne e cada kg custa R$82.40\n"
                f"Recomendo comprar {qtddcarne} kg de carne\n"
                f"O custo total será de R${custototal:.2f}\n"
                f"Cada pessoa pagará {custototal / self.pessoas:.2f}")


c1 = Churrasco("Churrasco dos amigos", 15)
print(c1)