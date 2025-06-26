s= 0
for c in range(0,6):
    lista= ('primeiro', 'segundo', 'terceiro','quarto','quinto','sexto','setimo','oitavo','nono','decimo')
    num= int(input('Informe o {} número: '.format(lista[c])))
    if num%2==0:
        s += num
print ('A soma dos valores pares digitados é {}'.format(s))