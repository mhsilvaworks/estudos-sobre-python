from datetime import date
atual =date.today().year 
lista= ('primeira', 'segunda', 'terceira','quarta','quinta','sexta','setima')
print ('Estamos no ano de {}'.format(atual))
mai =0
men =0

for c in range(0, 7):
    ano =int (input('E que ano a {} pessoa nasceu? '.format(lista[c])))
    if (atual -18)<= ano:
        mai+=1
    else:
        men +=1
print('Ao todo tivemos {} pessoas maiores de idade \n E também tivemos {} pessoas menores de idade'.format(mai, men))
    