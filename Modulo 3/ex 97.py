def escreva(msg):
    print('~'*(2+len(msg)))
    print(f' {msg} ')
    print('~'*(2+len(msg)))
msg = str (input('Escreva a sua mensagem para realizar o print: '))
escreva(msg)
