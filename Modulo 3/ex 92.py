#  programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
from time import sleep
x = {
    'nome': str(input('Nome: ')),
    'idade': datetime.now().year -int(input('Ano de nascimento: ')),
    

}
nc = int(input('Informe o número da carteira de trabalho(0 caso não tenha): '))
if nc != 0:
    x['Número dad carteira de trabalho'] = nc
    x['aposentadoria'] = datetime.now().year -int(input('Informe o ano de contratação: ')) +35 + x['idade'] 
    x['salário'] = int (input('Informe o salário: '))
print('-='*30)
for k,v in x.items():
    print(f'O {k} tem valor de {v}')
    sleep(0.4)
    

