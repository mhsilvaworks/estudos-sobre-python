nota1 = float(input('Qual foi a sua primeira nota: '))
nota2 = float(input('Qual foi a sua segunda nota: '))
media = (nota1+nota2)/2
if media < 5.0:
    print('\033[31mREPROVADO\033[m')
else:
    if media <=6.9 and media>= 5.0:
        print('\033[33mRECUPERAÇÃO\033[m')
    else:
        if media >= 7.0:
            print('\033[32mAPROVADO\033[m')
        
