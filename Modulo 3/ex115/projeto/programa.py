from interface import *
from arquivo import *

arq ='Cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArq(arq)
while True:
    x = menu()
    if x ==3:
        saindo()
        break 
    elif x ==1:
        lerArquivo(arq)
    elif x==2:
        cabeçalho('\033[34;1mCadastrar nova pessoa\033[m')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome,idade)
        