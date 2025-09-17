#Escreva um programa que determine o preço da passagem baseado na idade.

print("===== Passagem de Ônibus =====")
idade = int(input("Digite a sua idade: "))

if (idade < 6 or idade > 59):
   print("passagem gratuita!")
elif (idade > 5 and idade < 18):
   print("Passagem: R$2,50")
else:
   print("Passagem: R$5,00")