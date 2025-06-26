print('-=-='*20)
valordacasa = float (input('Qual é o valor da casa: '))
salario = float (input('Qual é o salário: '))
anos = int (input('Em quantos anos ele pretende pagar as prestações: '))

valor_mensal = valordacasa /(anos *12)
if valor_mensal > (salario*0.30):
    print('O emprestimo foi negado')
    print('MOTIVO: O seu salário mensal não é suficiente, você deve ter uma renda mensal de no mínimo R${:.2f}'.format((valor_mensal/3)*10))
else:
    print ('O emprestimo de R${:.2} foi aprovado.'.format(valordacasa))