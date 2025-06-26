print('='*25)
print("  10 TERMOS DE UMA PA  ")
print('='*25)
pt= int (input('Informe o primeiro termo: '))
r= int (input('Informe a razão: '))
dec= pt +(10-1)  *r
for c in range (pt,dec +r,r):
    print('{}'.format(c), end=' - ')
print ('FIM')
