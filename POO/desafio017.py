''' Desafio 017 - Crie uma classe Produto e implemente uma etiqueta de preço formatada, utilizando métodos especiais, atributos
de instância e, opcionalmente, a biblioteca Rich para exibição visual.'''
from rich import print
from rich.panel import Panel
class Produto:

    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def etiqueta(self):
        precof = f"R$ {self.valor:.2f}"
        conteudo = f"{self.nome.center(70, '.')}\n{precof.center(70, '-')}"
        etiqueta = Panel(conteudo, title="Produto", width=75)
        return etiqueta

produto1 = Produto("iPhone 17 Pro Max", 25000.85)
produto2 = Produto("Notebook Gamer", 8500)
print(produto1.etiqueta())
print(produto2.etiqueta())
