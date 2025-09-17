#Escreva um programa que simule uma calculadora simples.

print("=========== Calculadora ===========")
n1 = float(input("Digite o primeiro número: "))
sinal = input("Digite o sinal de cálculo exemplo: + , - , * , / : ")
n2 = float(input("Digite segundo número: "))

if (sinal == "+"):
  result = n1 + n2
elif (sinal == "-"):
  result = n1 - n2
elif (sinal == "*"):
  result = n1 * n2
elif (sinal == "/"):
  result = n1 / n2
else:
  print("O sinal não foi digitao corretamente")

print("O resultado é =",result)