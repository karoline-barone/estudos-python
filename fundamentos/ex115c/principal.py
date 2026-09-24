'''Ex115 - Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto
simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
Parte c - Finalizando o projeto de acesso a arquivos em Python'''
from ex115c.biblioteca.interface import *
from ex115c.biblioteca.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    match resposta:
        case 1:
            lerArquivo(arq)
        case 2:
            cabecalho('NOVO CADASTRO')
            nome = str(input('Nome: '))
            idade = leiaInt('Idade: ')
            cadastrar(arq, nome, idade)
        case 3:
            cabecalho('Saindo do sistema...')
            break
        case _:
            print('\033[31mErro! Digite uma opção válida\033[m')
    sleep(2)
