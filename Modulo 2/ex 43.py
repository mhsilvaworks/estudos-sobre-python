altura = float (input('Qual é a sua altura: '))
peso = float (input('Qual é o seu peso: '))
IMC = peso/ (altura*altura) 
if IMC <= 40:
    if IMC < 30:
        if IMC <25:
            if IMC <18.5:
                print('Abaixo do peso')
            else:
                print('Peso ideal')
        else:
            print('Sobrepeso')
    else:
        print('Obesidade')
else:
    print('Obesidade mórbida')
print ('E seu IMC é igual a {}'.format(IMC))