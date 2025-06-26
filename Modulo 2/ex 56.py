lista= ('primeira', 'segunda', 'terceira','quarta','quinta')
old = ''
midade= 0 
media =0
cont=0
for c in range (0, 4):
    print('----- {} PESSOA -----'.format(lista[c].upper()))
    nome = str(input ('Nome: '))
    idade = int (input('Idade: '))
    sexo = str (input ('Sexo [M/F]: '))
    media += idade
    if idade > midade and sexo == 'M':
        old = nome
        midade =idade
    if sexo =='F' and idade < 20:
        cont +=1


media = media/4
print('-='*40)
print('A média de idade do grupo é {}\nO homem mais velho do grupo é o {} dfcom {} anos\nO grupo possue {} mulheres com idade menor que 20 anos'.format(media,old,midade,cont))
print('-='*40)