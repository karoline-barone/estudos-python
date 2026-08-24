'''Desafio 016 - Crie a classe Funcionario, onde podemos cadastrar nome, setor e cargo. Crie também um metodo que permita
ao funcionário se apresentar.'''
class Funcionario:

    empresa = "Curso em Vídeo"

    def __init__(self, nome = '', setor = '', cargo = ''):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self) -> str:
        return f"Olá! Meu nome é {self.nome}, trabalho no setor {self.setor} como {self.cargo} na {self.empresa}."


funcionario1 = Funcionario("Gustavo", "Ensino", "Professor")
print(funcionario1.apresentar())

funcionario2 = Funcionario("Gabriel", "TI", "Programador")
print(funcionario2.apresentar())
