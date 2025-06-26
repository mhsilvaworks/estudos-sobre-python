num = int (input('Informe um número para a conversão: '))
A = int (input('Você deseja converter para que base 1(binário) 2(octa) 3(hexadecimal)? '))

if A==1:
    
    print(bin(num)[2:])
else: 
    if A == 2:
        print(oct(num)[2:])
    else:
        if A== 3: 
            print(hex(num)[2:])