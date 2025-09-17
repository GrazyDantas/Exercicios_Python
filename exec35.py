#Crie um programa que determine o tipo de triângulo.

l1 = int(input("Digite o prmeiro lado do triangulo: "))
l2 = int(input("Digite o segundo lado do triangulo: "))
l3 = int(input("Digite o terceiro lado do triangulo: "))

if (l1 == l2 & l2 == l3 & l1 == l3):
  print("Triângulo Equilátero")
elif (l1 != l2 & l2 != l3 & l3 != l1):
  print("Triângulo Escaleno")
else:
  print("Triângulo isóceles")