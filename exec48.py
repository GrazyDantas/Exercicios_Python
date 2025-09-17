#Escreva um programa que determine o maior e menor entre três números.

n1 = int(input("Digite o 1°numero: "))
n2 = int(input("Digite o 2°numero: "))
n3 = int(input("Digite o 3°numero: "))

if (n1 >= n2 and n1 >= n3):
   print("O maior número é:", n1)
elif (n2 >= n1 and n2 >= n3):
   print("O maior número é:", n2)
else:
   print("O maior número é:", n3)