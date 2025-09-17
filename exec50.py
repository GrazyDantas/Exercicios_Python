#Escreva um programa que verifique se três lados podem formar um triângulo e classifique-o

l1 = int(input("Digite o prmeiro lado do triangulo: "))
l2 = int(input("Digite o segundo lado do triangulo: "))
l3 = int(input("Digite o terceiro lado do triangulo: "))

if (l1 + l2 > l3):
   if (l1 == l2 & l2 == l3 & l1 == l3):
     print("Forma um triângulo Equilátero")
   elif (l1 != l2 & l2 != l3 & l3 != l1):
     print("Forma um triângulo Escaleno")
   else:
     print("Forma um Triângulo isóceles")
else:
   print("Não forma um triângulo")