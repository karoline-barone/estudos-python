'''Desafio022 - Crie a classe ControleRemoto, onde vamos simular o funcionamento de um controle simples (canal, volume e liga/desliga)'''
from rich import print
from rich.panel import Panel
from rich.text import Text
class ControleRemoto:
    canal_min = 1
    canal_max = 5
    volume_min = 1
    volume_max = 5

    def __init__(self, canal = 1, volume = 1):
        self.canal_atual = canal
        self.volume_atual = volume
        self.ligado = False

    def liga_desliga(self):
        self.ligado = not self.ligado

    def mostrartv(self):
        if not self.ligado:
            conteudo = "A TV está desligada"
            tv = Panel(conteudo, title="[TV]", width=30)
        else:
            conteudo = f"CANAL: "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max +1):
                if canal == self.canal_atual:
                    conteudo += f" [black on green] {canal} [/] "
                else:
                    conteudo += f" {canal} "
            conteudo += f"VOLUME: "
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max +1):
                if volume <= self.volume_atual:
                    conteudo += f" [black on green] [/] "
                else:
                    conteudo += f" [black on white] [/] "
            tv = Panel(conteudo, title="[TV]", width=30)
        print(tv)

    def canalmais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    def canalmenos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    def volumemais(self):
        if self.ligado:
            if self.volume_atual == ControleRemoto.volume_max:
                self.volume_atual = ControleRemoto.volume_max
            else:
                self.volume_atual += 1

    def volumemenos(self):
        if self.ligado:
            if self.volume_atual == ControleRemoto.volume_min:
                self.volume_atual = ControleRemoto.volume_min
            else:
                self.volume_atual -= 1


c = ControleRemoto()
while True:
    c.mostrartv()
    comando = str(input(f"\n< CH >  - VOL +  "))
    match comando:
        case '0':
            break
        case '@':
            c.liga_desliga()
        case '<':
            c.canalmenos()
        case '>':
            c.canalmais()
        case '-':
            c.volumemenos()
        case '+':
            c.volumemais()
