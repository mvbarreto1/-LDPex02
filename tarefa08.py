frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

if palavra in frase:
    resultado = "A palavra está presente na frase."
else:
    resultado = "A palavra não está presente na frase."

print(resultado)
