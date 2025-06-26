from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 9:
    print('MIRIM')
elif idade < 14:
    print('INFANTIL')
elif idade < 19:
    print('JUNIOR')
elif idade < 25:
    print('SÊNIOR')
else:
    print('MASTER')
