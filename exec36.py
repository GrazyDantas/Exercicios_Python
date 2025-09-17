#Escreva um programa que verifique se uma senha é válida.

sugestao = ""

while sugestao != "fatec":
  sugestao = input("Digite uma senha: ")
  if sugestao != "fatec":
    print("Senha inválida, tente novamente!")

print("A senha está correta!")