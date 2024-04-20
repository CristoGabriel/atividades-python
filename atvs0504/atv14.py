def obter_preco(produto):
    return produto['preço']

produtos = [
    {'descrição': 'é roxa','preço': 2,},
    {'descrição': 'é vermelha','preço': 3,},
    {'descrição': 'é amarela','preço': 4,},
    {'descrição': 'é azul','preço': 5,},
    {'descrição': 'é verde','preço': 6,},
]
pc = max(produtos, key=obter_preco)

pb = min(produtos, key=obter_preco)

print("Produto mais caro:")
print("Descrição:", pc["descrição"])
print("Preço: R$", pc["preço"])

print("\nProduto mais barato:")
print("Descrição:", pb["descrição"])
print("Preço: R$", pb["preço"])
