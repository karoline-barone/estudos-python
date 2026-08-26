'''Desafio019 - Crie a classe livro que vai simular a passagem de páginas de um livro, considerando também se o usuário chegou ao fim da leitura.'''
class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.pagina_atual = 1
        print(f"Você acabou de abrir o livro {self.titulo} que tem {self.paginas} páginas no total. Agora você está na página {self.pagina_atual}.")

    def avancar_paginas(self, qtd_paginas):
        pag = self.pagina_atual + qtd_paginas
        while self.pagina_atual < pag and self.pagina_atual < self.paginas:
            self.pagina_atual += 1
            print(f"Pag{self.pagina_atual} --> ", end="")
        print(f"Agora você está na página {self.pagina_atual}.")
        if(self.pagina_atual == self.paginas):
            print(f"Você chegou ao fim do livro {self.titulo}.")

l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(2)
l1.avancar_paginas(3)
l1.avancar_paginas(10)
l1.avancar_paginas(20)
