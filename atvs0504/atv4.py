lista = []

for p in range(5):
    nome = input('Digite um nome: ')
    lista.append(nome)

for nome in lista:
    print(nome)

numero = int(input('Informe um número: '))
del lista[numero]

for nome in lista:
    print(nome)