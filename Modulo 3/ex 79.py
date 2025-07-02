num = list()
x=''
while True:
    n = int(input('Digite o número: '))
    if n not in num:
        print(f'O número {n} foi salvo coom sucesso')
        num.append(n)
    else:
        print(f'O número {n} já foi informado, favor não inserir dados duplicados.')
        
    
    x = str(input('Você deseja continuar?[S/N]?')).strip()[0]
    if x in 'Nn':
        break
num.sort()
print (f'Você digitou os valores {num}')


        
