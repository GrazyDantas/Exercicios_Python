#Crie um programa que verifique se uma data é válida (formato simples).

dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if (dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and ano > 0 and ano <= 2025):
   print("A data",dia,"/",mes,"/",ano,"é valida")
else:
   print("O Formato da data é inválido")