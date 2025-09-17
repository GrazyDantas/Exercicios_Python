#Crie um programa que determine o maior entre três números.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if (n1 > n2 and n2 > n3):
  print(n1,"é maior que",n2,"e",n3)
elif (n1 < n2 and n2 > n3):
  print(n2,"é maior que",n1,"e",n3)
else:
  print(n3,"é maior que",n2,"e",n1)