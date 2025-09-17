#Escreva um programa que calcule a potência de um número.

base = int(input("Digite um número: "))
potencia = int(input("Digite o valor da potência: "))

vezes = 0
result = 1

while (vezes < potencia):
  result *= base
  vezes += 1

print("O resultado é:",result)