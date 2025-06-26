print('_'*30)
print('Sequencia de Fibonacci')
print('-'*30)
x =int(input('Quantos termos deseja mostrar? '))
print('~'*3*x)
t1 = 0 
t2 = 1
t3 = 1
print('{} - {}'.format(t1,t2), end='')
cont = 3
while cont <= x:
    t2 = t1
    t1 = t3
    t3 = t1 + t2
    
    
    print (' - {}'.format(t3), end='')
    cont +=1
print (' - FIM')


