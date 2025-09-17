#Escreva um programa que compare duas strings.

p1 = input("Digite uma palavra: ")
p2 = input("Digite outra palavra: ")

l1 = len(p1)
l2 = len(p2)

if (p1 == p2 or l1 == l2):
   print(p1,"é igual a",p2)
else:
   print(p1,"é diferente de",p2)