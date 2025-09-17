#Crie um programa que verifique se um número é múltiplo de outro.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if (n1 % n2 == 0):
   print(n1,"é multiplo de",n2)
else:
   print(n1,"não é multiplo de",n2)