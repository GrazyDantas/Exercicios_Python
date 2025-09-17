#Crie um programa que calcule o salário líquido com base no salário bruto.

sal = float(input("Digite o valor do salário bruto: "))

if (sal > 1000 and sal < 5000):
   sal = sal - (sal * 0.05)
elif (sal >= 5000 and sal < 10000):
   sal = sal - (sal * 0.10)
elif (sal > 10000):
   sal = sal - (sal * 0.15)

print("O salário líquido é:",sal)