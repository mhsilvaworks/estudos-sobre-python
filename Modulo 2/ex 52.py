cont= 0
num = int(input('Digite um número inteiro: '))
for c in range(1,num +1):
    if num %c ==0:
        cont += 1
        print ('\033[32m',end='')
    else:
        print ('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n \033[mO número {} foi divisível {} vezes'.format(num, cont))
if cont >=2:
    print('{} é um número primo'.format(num))
else:
    print('{} não é um número primo'.format(num))