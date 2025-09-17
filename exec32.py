#Escreva um programa que calcule o IMC e classifique o resultado.

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: ")

imc = peso / (altura * altura)

if (imc <= 18.5):
  print("Seu imc é: %.2f Subpeso" %imc)
elif(imc >= 18.6 and imc <= 24.99):
  print("seu imc é: %.2f saldável" %imc)
elif(imc >= 25.0 and imc <= 29.99):
  print("seu imc é: %.2f Sobrepeso" %imc)
elif(imc >= 30.0 and imc <= 40.0):
  print("seu imc é: %.2f Obesidade" %imc)
else:
  print("seu imc é: %.2f Obesidade extrema" %imc)