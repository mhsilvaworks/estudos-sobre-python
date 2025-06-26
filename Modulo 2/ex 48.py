s = int(0)
for c in range(1, 501):
    if c%3 == 0:
        s +=c
        print(c)
print('A soma de todos os números entre 1 e 500 é {}'.format(s))