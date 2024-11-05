idade = int(input("Digite sua idade:"))
habilitaçao = input("Você possui habilitação ? (sim/não):")

if idade >=18 and habilitaçao == "sim":
    resultado = "Maior de idade habilitado"

elif idade < 18 :
    resultado = "Menor de idade (Não possuem habilitação)"

else:
    resultado = "Maior de idade não habilitado"

print(resultado)