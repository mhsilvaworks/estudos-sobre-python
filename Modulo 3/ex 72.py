n=-1
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int (input('Informe um número para ser escrito por extenso: '))

while n < 0 or n > 20:
   n = int (input('Tente novamente. informe um número de 0 a 20: '))
    
print(numeros[n])









