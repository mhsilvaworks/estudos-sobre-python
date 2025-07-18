def leiaInt(pergunta):
    while True:        
        try:
            x = int(input(pergunta))  
        except(ValueError, TypeError):
            print('\033[31mErro: o dado informado é inválido.\033[m')
        except(KeyboardInterrupt):
            print('\n\033[33mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:        
            return x
def leiaFloat(pergunta):
    while True:
        try:
            x = float(input(pergunta))
        except(ValueError, TypeError):
            print('\033[31mErro: o dado informado é inválido.\033[m')
        except(KeyboardInterrupt):
            print('\n\033[33mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:        
            return x
x = leiaInt('Informe um número Inteiro: ')
y = leiaFloat('Informe um número Real: ')
print(f'O usúario digitou o número {x} como o valor inteiro e o valor {y} como o valor real.')