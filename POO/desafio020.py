'''Desafio020 - Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa. Crie também um
metodo que permita mostrar a ficha desse gamer'''
from rich import print
from rich.panel import Panel
class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_favoritos(self, jogo):
        self.jogos_favoritos.append(jogo)
        self.jogos_favoritos.sort()

    def etiqueta(self):
        jogos_formatados = "->" + "\n->".join(self.jogos_favoritos)
        conteudo = f"Nome real:{self.nome}\nJogos favoritos:\n{jogos_formatados}"
        etiqueta = Panel(conteudo, title=f"Jogador<{self.nick}>", width=40)
        return etiqueta

g1 = Gamer("Fabricio da Silva", "detonador2025")
g1.add_favoritos("Mario Bros")
g1.add_favoritos("God Of War")
g1.add_favoritos("Sonic")
g1.add_favoritos("Fortnite")
print(g1.etiqueta())

g2 = Gamer(nome="Olivia Souza", nick="peach_raivosa")
g2.add_favoritos("Mario Bros")
g2.add_favoritos("Call of Duty")
print(g2.etiqueta())
