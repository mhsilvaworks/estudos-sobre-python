from time import sleep
def saindo():
            print('Saindo do sistema', end='',flush=tuple)
            sleep(0.6)
            print('.',flush=tuple, end='')
            sleep(0.6)
            print('.',flush=tuple, end='')
            sleep(0.6)
            print('.',flush=tuple, end='')    
def opção(x,y):
    print(f'\033[43;7m{x}', end='\033[43;7m - \033[m')
    print(f'\033[44;7m{y:<26}\033[m')

def cabeçalho(msg):
    print('='*30)
    print(f'{msg:^30}')
    print('='*30)
def leiaopção(f):
    while True:
        try:
            x = int(input(f'\033[33m{f}\033[m'))
        except(TypeError,ValueError):
            print('\033[31;1mErro: \033[31;0m\033[31;4mInforme um número inteiro válido que corresponda a uma das opções.')
        else:
            if x == 1 or x ==2 or x==3:
                return x  
            else:
                print (f'\033[31;1mErro: \033[31;0m\033[31;4mO valor {x} não corresponde a nenhuma das opções.\033[m')
def menu():   
    while True:
        print('\033[7m-\033[m'*30)
        print(f'\033[7m|{'MENU PRINCIPAL':^28}|\033[m')
        print('\033[7m-\033[m'*30)
        opção(1,'Ver pessoas cadastradas.')
        opção(2,'Cadastrar nova pessoa.')
        opção(3,'Sair do programa.')
        print('\033[7m-\033[m'*30)
        x = leiaopção('Opção: ')
        
        if x == 1 or x == 2 or x==3:
            return x
