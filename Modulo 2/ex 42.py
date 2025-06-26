r1 = float (input('Primeiro segmento: '))
r2 = float (input('Segmento segmento: '))
r3 = float (input('Tercerio segmento: '))
if r1 < r2 + r3 and r2 < r2 + r3 and r3< r1 +r2:
    print ('Os segmentos acima podem formar um triângulo!')
    if r1== r2 ==r3:
        print ('Equliatero')
    else: 
        if r1 != r2 != r3 != r1:
            print ('Escaleno')
        else:
            print('Isosceles')

else:
    
    print ('segmentos acima não podem formas triâgulo')
