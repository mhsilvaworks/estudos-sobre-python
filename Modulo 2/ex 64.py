num  =0
total  =0  
cont= 0
while num != 999:
    num = int (input('Difite um número [999 para parar]: '))
    if num != 999:
        total=num +total
        cont += 1
print ('A soma dos {} números informados é {}'.format(cont, total))
        
