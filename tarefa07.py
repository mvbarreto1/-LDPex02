frase = input("Digite uma frase: ")
caractere = input("Digite um caractere: ")

if caractere in frase:
    resultado = "O caractere está presente na frase."
else:
    resultado = "O caractere não está presente na frase."

print(resultado)
