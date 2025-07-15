def aumentar(v=0, p=0):
    r=(v*((100+p)/100))  
    return r
def diminuir(v=0, p=0):
    r= v*((100-p)/100)
    return r
def dobro(v=0):
    r  = v*2
    return r
def metade(v=0):
    r = v/2
    return r
def moeda(p= 0, m ='R$'):
    p = float(p)
    return f'{m}{p:.2f}'.replace('.',',') 