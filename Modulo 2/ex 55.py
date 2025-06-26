lista= ('primeira', 'segunda', 'terceira','quarta','quinta')
mai =0
men =0
for c in range(0,5):
    pe = float(input('Informe o  da {} pessoa: '.format(lista[c])))
    if c ==0:
        men =pe
    if pe >= mai:
        mai =pe
    else:
        if pe < men:
            men = pe
print('O menor peso foi {} \n E o maior peso foi {}'.format(men, mai))