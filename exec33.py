#Crie um programa que verifique se um número está em um intervalo.

num = int(input("Digite um numero: "))

if (num >= 1 and num <= 100):
  print(num,"está no intervalo")
else:
  print(num,"não está no intervalo")