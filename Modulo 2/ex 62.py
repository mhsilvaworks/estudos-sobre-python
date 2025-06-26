print('              Greador de PA\n=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
n1= int(input('Primeiro termo: '))
r = int (input('Razão da PA: '))
termo = n1
cont =1
total =0 
mais= 10
while mais!=0:
    total = total +mais
    while cont <= total:
        print('{}-'.format(termo),end='')
        termo +=r
        cont +=1
    print ('PAUSA')
    mais = int(input('Quantos termos você quer gerar a mais? '))
print ('Progressão finalizada com sucesso, com {} termos gerados'.format(total))