#Crie um programa que determine o desconto baseado no valor da compra.

preco = float(input("Digite o preço do produto: "))

if (preco < 50):
  desconto = preco - (preco * 0.05)
elif (preco >= 50 and preco <= 100):
  desconto = preco - (preco * 0.10)
elif (preco > 100):
  desconto = preco - (preco * 0.15)

print("O preço",preco,"com desconto sai por: %.2f" #desconto)