print ('='*21)
print('        BANCO')
print ('='*21)
print('')
a =0
d= int(input('Informe quanto você deseja sacar: '))
if d>= 100:
    a= d//100
    d = d-(a*100)
    print (f'{a} notas de 100')

if d >=50:
    a= d //50
    d=d-(a*50)
    print (f'{a} notas de 50')
if d >=20:
    a= d //20
    d=d-(a*20)
    print (f'{a} notas de 20')
if d >=10:
    a= d //10
    d=d-(a*10)
    print (f'{a} notas de 10')
if d >=5:
    a= d //5
    d=d-(a*5)
    print (f'{a} notas de 5')
if d >=2:
    a= d //2
    d=d-(a*2)
    print (f'{a} notas de 2')
if d >=1:
    a= d
    
    print (f'{a} notas de 1')

    


