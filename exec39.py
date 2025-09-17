#Crie um programa que simule um sistema de login.

print("============== Crie uma conta ============== ")
user = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

usert = ""
senhat = ""
print("============== Login ============== ")
while (senhat != senha or usert != user):
   usert = input("usuário: ")
   senhat = input("senha: ")
   if (usert == user and senhat == senha):
      print("Logando...")
   else:
      print("usuário ou senha incorreta, por favor tente novamente!\n")

print("Login efetuado com sucesso!")