numero = float(input("Digite um número: "))

if numero % 2 == 0:
    x = "par"
else:
    x = "ímpar"

if numero > 0:
    sinal = "positivo"
elif numero < 0:
    sinal = "negativo"
else:
    sinal = "zero"

print(f"O número {numero} é {x} e {sinal}.")
