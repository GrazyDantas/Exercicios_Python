#Escreva um programa que calcule a hipotenusa de um triângulo retângulo.

cateto1 = float(input("Digite o tamanho do cateto1: "))
cateto2 = float(input("Digite o tamanho do cateto2: "))

hipotenusa = ((cateto1 * cateto1) + (cateto2 * cateto2)) ** 0.5

print("A hipotenusa é:",hipotenusa)