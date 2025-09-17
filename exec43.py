#Crie um programa que verifique se um número é divisível por 3 e por 5.

n = int(input("Digite um número: "))

if (n % 3 == 0 and n % 5 == 0):
   print(n,"é divisível por 3 e por 5")
else:
   print(n,"não é divisivel por 3 e por 5")