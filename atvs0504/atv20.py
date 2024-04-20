def maio():
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite um numero: '))
    n3 = int(input('Digite um numero: '))

    maior = 0

    if n1 > n2 and n3:
        maior = n1
        print(maior)
    elif n2 > n1 and n3:
        maior = n2
        print(maior)
    else:
        maior = n3
        print(maior)

maio()