idade = int(input('digite a idade: '))

if idade >= 0 and idade <= 11:
    print('criança.')
elif idade >= 12 and idade <= 18:
    print('adolescente')
elif idade >= 19 and idade <= 24:
    print('jovem')
elif idade >= 25 and idade <= 40:
    print('adulto')
elif idade >= 41 and idade <= 60:
    print('meia idade')
elif idade > 60 :
    print('idoso')
else:
    print('idade invalida')

