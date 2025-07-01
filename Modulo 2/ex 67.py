while True:
    cont=1
    n = int (input('Qual número você deseja ver a tabuada: '))
    if n <0:
        break
    while 11 > cont:
        print(f'{n}x{cont} = {n*cont}')    
        cont+=1
    
    
print('-='*27)
print ('Programa encerrado')

