print('========== LOJA DA TANANAN ==========')
print('Seja bem_vindo(a) a loja com o melhor nome do mundo!!')
preco = float(input('Preço das compras: '))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheirocheque \n [ 2 ] à vista cartão \n [ 3 ] 2x no cartão \n [ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))
if opcao ==1:
    print('Você recebeu um desconto de 10%, logo a sua conta que seria de R${:.2f} passoou a ser R${:.2f}'.format(preco, preco*0.90))
else:
    if opcao ==2:
        print('Você recebeu um desconto de 5%, logo a sua conta que seria de R${:.2f} passou a ser R${:.2f}'.format(preco, preco *0.95))
    else:
        if opcao ==3:
             print('Você escolher pagar 2 vezes no cartão, logo a sua conta que seria de R${:.2f} passou a ser duas vezes de R${:.2f}'.format(preco, preco *0.5))
        else:
            if opcao == 4:
                nump= int (input('Qual será o número de parcelas: '))
                print('Você optou por parcelar em {} vezes com juros de 20%, logo a sua conta que seria de R${:.2f} passou a ser R${:.2f}, que será dividido em parcelas de R${}'.format(nump, preco, preco *1.20, (preco*1.20)/nump))
            else:
                print ('\033[31mOPÇÃO INVÁLIDA\033[m')
                print('O valor {} não é uma opção válida'.format(opcao))
nome= str(input('what is your name: '))
if nome == 'Gabi':
    print(' Pode ficar tranquila minha rainha a sua conta é por conta do seu malidu.')
else:
    print(' Infelizmente para você não tem vida fácil se vira e paga')
