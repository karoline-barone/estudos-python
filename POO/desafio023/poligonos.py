from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return self.lado * 4

class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)

    def perimetro(self):
        return 2 * 3.14 * self.raio
