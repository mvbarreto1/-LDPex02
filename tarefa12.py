peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 24.9 <= imc < 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}.")
