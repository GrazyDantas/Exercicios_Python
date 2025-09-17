#Crie um programa que simule um jogo de adivinhação.

print("========== Adivinhe a palavra ==========")
print("Dica 1: é um inseto")
print("Dica 2: pode ter diversas cores")
print("Dica 3: vive em plantas e pode voar")

sugestao = ""
while (sugestao != "joaninha"):
   sugestao = input("Digite a sua sugestão: ")
   print("errou! tente novamente")

print("você acertou! A palavra é joaninha 🐞")