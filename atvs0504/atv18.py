
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
n4 = int(input('Digite um numero: '))

def maio():
    if  n1 > n2 and n3 and n4:
        n1 * 2
        print(n1)
    elif n2 > n1 and n3 and n4:
        n2 * 2
        print(n2)
    elif n3 > n2 and n1 and n4:
        n3 * 2
        print(n3)
    elif n4 > n2 and n3 and n1:
        n4 * 2
        print(n4)
    else:
        print('existem números iguais')

maio()