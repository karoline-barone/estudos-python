from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, nome):
        self.nome = nome
        self.inss = 7.5
        self.sal_min = 1612


    @abstractmethod
    def calc_sal(self):
        pass

    @abstractmethod
    def analisar_sal(self):
        pass


class Mensalista(Funcionario):

    def __init__(self, nome, sal_bruto):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario_final = self.sal_bruto * ((100 - self.inss) / 100)
        print(f"O salário recebido por {self.nome} com descontos é R${self.salario_final:.2f}")

    def analisar_sal(self):
        self.analise = self.salario_final / self.sal_min
        print(f"O salário recebido por {self.nome} corresponde a {self.analise:.1f} salários mínimos")


class Horista(Funcionario):

    def __init__(self, nome, valor_hora, qtd_horas):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.qtd_horas = qtd_horas

    def calc_sal(self):
        self.salario_final = self.valor_hora * self.qtd_horas * ((100 - self.inss) / 100)
        print(f"O salário recebido por {self.nome} com descontos é R${self.salario_final:.2f}")

    def analisar_sal(self):
        self.analise = self.salario_final / self.sal_min
        print(f"O salário recebido por {self.nome} corresponde a {self.analise:.1f} salários mínimos")
