#Crie um programa que converta segundos em horas, minutos e segundos.

segundos = int(input("Digite uma quantidade de segundos: "))

minutos = segundos / 60
horas = minutos / 60

print("Segundos:",segundos)
print("Minutos:",minutos)
print("Horas:%.2f"%horas)