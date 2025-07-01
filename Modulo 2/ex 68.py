from random import randint
from time import sleep

    
print('========= IMPAR OU PAR =========')
cont=0
while True:
    computador = randint(1,10)
    
    num= int(input('Digite um valor: '))
    o = str (input('Impar ou Par: ')).upper()[0]
    print('Pensando', end='')
    sleep(0.2)
    print('.', end=' ')
    sleep(0.5)
    print('.', end=' ')
    sleep(0.5)
    print('.')
    if (num + computador) %2 ==0:
        if o == 'P':
            print ('você ganhouuuu!!!!!!!!!')
            cont +=1
        else:
            print ('Você perdeu ')
            print(f'O computador jogou {computador}')
            break
    else:
        if o =='I':
            print ('você ganhouuuu!!!!!!!!!')
            cont+=1
        else:
            print ('Você perdeu ')
            print(f'O computador jogou {computador}')
            break
if cont <= 0:
    print ('Que azar infelismente você não ganhou nenhuma vez')
else:
    print(f'Parabéns você ganhou {cont} vezes')
    

