from interface import *
def arquivoExiste(arq):
    try:
        x = open(arq, 'rt')
        x.close
    except FileNotFoundError:
        return False
    else:
        return True
def criarArq(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print(f'\033[31mFalha ao criar o arquivo "{nome}"\033[m')
    else:
        print(f'O arquivo "{nome}" foi criado com sucesso.')
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Falha ao tentar abrir o arquivo')
    else:
        cabeçalho('\033[34;1mPessoas cadastradas\033[m')
        for linha in a:
            dado= linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:.<28}{dado[1]}')
    finally:
        a.close()
def cadastrar(arq,nome='<desconhecido>', idade=0):
    try:
        a =open(arq,'at')
    except:
        print('houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'\033[31mHouve um erro ao tentar informar os dados de {nome}\033[m')
        else:
            print(f'\033[32mOs dados de {nome} foram adicionados com sucesso\033[m ')