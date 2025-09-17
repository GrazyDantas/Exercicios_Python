#Escreva um programa que classifique a temperatura.

print("============= Temperatura Corporal =============")
temperatura = float(input("Digite a temperatura: "))

if (temperatura < 36):
  print("Hipotermia")
elif (temperatura >= 35 and temperatura <= 37.5):
  print("Temperatura normal")
elif (temperatura >= 37.6 and temperatura <= 39.5):
  print("Febre")
elif (temperatura >= 39.6 and temperatura <= 41):
  print("Febre alta")
else:
  print("Hipertermia")