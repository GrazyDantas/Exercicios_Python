#Escreva um programa que classifique a nota de um aluno.

nota = float(input("Digite a sua nota: "))

if(nota >= 7.0):
  print("Nota boa!")
elif (nota >= 5.0 and nota < 6.9):
  print("Nota mediana")
elif (nota < 5.0):
  print("Nota baixa")