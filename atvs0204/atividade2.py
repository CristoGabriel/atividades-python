n = int(input('digite uma idade: '))
if n < 13 and n > 0:
    print('criança')
elif n > 12 and n < 19:
    print('adolescente')
elif n > 18:
    print('adulto')
else:
    print('idade inválida')
