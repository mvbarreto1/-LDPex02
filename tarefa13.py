nome_usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if nome_usuario == "admin" and senha == "1234":
    print("Login bem-sucedido!")
else:
    print("Nome de usuário ou senha incorretos.")
