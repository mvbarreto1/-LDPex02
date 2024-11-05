preco_original = float(input("Digite o preço original do produto: R$ "))
quantidade = int(input("Digite a quantidade comprada: "))

total = preco_original * quantidade

if quantidade > 10:
    desconto = total * 0.10
    total -= desconto
    print(f"Desconto aplicado de 10%. Valor com desconto: R$ {total}")
else:
    print(f"Sem desconto aplicado. Valor total: R$ {total}")
