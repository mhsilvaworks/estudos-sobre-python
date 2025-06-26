num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1> num2:
    print('\033[32mO primeiro valor é maior\033[m')
else:
    if num2> num1:
        print('\033[31mO segundo valor é o maior\033[m')
    else:
        print ('\033[33mNão existe valor maior, os dois são iguais\033[m')

