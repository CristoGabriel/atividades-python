n1 = float(input('digite um numero: '))
n2 = float(input('digite um numero: '))
oprc = (input('informe uma operação: '))


if oprc == '+' :
    print('soma: ',n1+n2)
elif oprc == '-' :
    print('subtração: ',n1-n2)
elif oprc == '/' :
    print('divisão: ',n1/n2)
elif oprc == '*' :
    print('multiplicação: ',n1*n2)
else:
    print('operação inválida')
