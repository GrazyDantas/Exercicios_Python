#Escreva um programa que calcule a distância entre dois pontos.

p1 = float(input("Digite o ponto 1 em cm: "))
p2 = float(input("Digite o ponto 2 em cm: "))

if (p1 > p2):
    distancia = p1 - p2
else:
    distancia = p2 - p1

print("A distância entre o ponto 1 e ponto 2 é:",distancia,"cm")
