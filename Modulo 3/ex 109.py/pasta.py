def aumentar(v=0, p=0, format= False):
    r=(v*((100+p)/100))  
    return r if format is False else moeda (r)
def diminuir(v=0, p=0,format= False):
    r= v*((100-p)/100)
    return r if format is False else moeda (r)
def dobro(v=0,format= False):
    r  = v*2
    return r if format is False else moeda (r)
def metade(v=0,format= False):
    r = v/2
    return r if format is False else moeda (r)
def moeda(p= 0, m ='R$',format= False):
    p = float(p)
    return f'{m}{p:.2f}'.replace('.',',') 