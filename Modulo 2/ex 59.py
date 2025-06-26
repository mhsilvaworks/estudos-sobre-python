o =0

num1 = int (input('Informe o primeiro número: '))
num2 = int (input('Informe o segundo valor: '))
while o != 5 :    
    print('--==='*24)
    o = int (input('O que você deseja fazer?\n[ 1 ] somar\n [ 2 ] multiplicar\n [ 3 ] maior \n[ 4 ] novas número\n[ 5 ] sair do programa\n >>>>>Qual é a sua opção? '))
    if o == 1:
        print ('O resultado da soma é {}'.format(num1 + num2)) 
    if o == 2:
        print ('O resultado da multiplicação é {}'.format(num1 * num2))
    if o == 3:
        if num1> num2:
            maior = num1
        else:
            maior = num2
        print ('Entre {} e {} o maior número é {}'.format(num1, num2,maior))
    if o == 4:
        num1 = int (input('Informe o primeiro número: '))
        num2 = int (input('Informe o segundo valor: '))
    if o == 5:
        print('Finalizando ...')
    else:
        if o >=5 or o <=0:
            print ('Opção inválida... Tente novamente. ')

print('--==='*24)
print('Fim do programa! Volte sempre!')
    
