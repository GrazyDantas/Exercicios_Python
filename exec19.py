#Escreva um programa que calcule juros simples.

capital = float(input("Digite o valor investido: "))
taxa = float(input("Digite o valor da taxa de juros: "))
tempo= float(input("Digite o tempo em meses: "))

taxaJuros = capital * taxa * tempo
capital = capital + taxaJuros

print("O valor do capital em",tempo,"meses é de:",capital)