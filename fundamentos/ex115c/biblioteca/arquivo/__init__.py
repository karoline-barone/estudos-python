from ex115c.biblioteca.interface import *

def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'Nome: {dado[0]:<15} Idade: {dado[1]:>3} anos')
    finally:
        arquivo.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        arquivo = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na inserção dos dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            arquivo.close()
