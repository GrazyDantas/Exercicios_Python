#Escreva um programa que determine o quadrante de um ponto no plano cartesiano.

x = int(input("Digite a coordenada x: "))
y = int(input("Digite a coordenada y: "))

if (x > 0 and y > 0):
   print("x e y pertence ao 1° quadrante")
elif (x < 0 and y > 0):
   print("x e y pertence ao 2° quadrante")
elif (x < 0 and y < 0):
   print("x e y pertence ao 3° quadrante")
else:
   print("x e y pertence ao 4° quadrante")