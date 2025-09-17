#Crie um programa que troque os valores de duas variáveis.

n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
print("Os números digitados em ordem foram",n1,"e",n2)

t = n1
n1 = n2
n2 = t

print("Agora a ordem é:",n1,"e",n2)