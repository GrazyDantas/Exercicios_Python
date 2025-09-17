#Crie um programa que calcule o desconto de um produto.

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a porcentagem de desconto: "))

novoPreco = preco - (preco * desconto)

print("O valor do produto com desconto fica:",novoPreco)