lista = []

for p in range(10):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        num += 100
    lista.append(num)

for num in lista:
    print(num)




