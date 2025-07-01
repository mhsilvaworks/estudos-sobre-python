soma= 0 
cont= 1
while True:
    num = int (input('Digite um número: '))
    if num == 999:
        break
    soma+=num
    cont += 1
print (f'Foram informados um total de {cont} números e a soma dele é igual a {soma}')