from datetime import date
ano = int(input('Qual é a sua data de nascimento: '))
idade = date.today().year -ano 
if idade == 18:
    print ('\033[32mEstá na hora de se alistar.\033[m')
else:
    if idade < 18:
        print('\033[34mAinda não é necessário se alistar, você deve se alistar daqui {} no ano de {}\033[m'.format(18-idade,18-idade+date.today().year))
    else:
        print ('\033[31mJá passou o tempo do seu alistamento, já passou {} anos do seu alistamento.\033[m'.format(idade-18))
