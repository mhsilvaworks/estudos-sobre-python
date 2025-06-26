from random import randint
itens=('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print ('=-=-'*20)
print ('PEDRA PAPEL TESOURA')
print ('=-=-'*20)
print ('Escolha a sua opção')
print ('[ 1 ] Pedra')
print ('[ 2 ] Papel')
print ('[ 3 ] Tesoura')
a = int (input('Informe a sua opção: '))
a = a-1
if a ==computador:
    print('Empate o computador tambem jogou {}'.format(itens[a]))
else:
    if 0 ==a:
        if computador ==1:
            print('Você perdeu, o computador jogou papel')
        else:
            print('Você ganhou, o computador joogou tesoura')
    else:
        if 1 == a:
            if computador ==0:
                print('Você ganhou, o computador jogou pedra')
            else:
                print('Você perdeu, o computador jogou tesoura')
        else: 
            if 2==a:
                if computador == 0:
                    print('você perdeu, o computador jogou pedra')
                else:
                    print('Você ganhou, o computador jogou papel')