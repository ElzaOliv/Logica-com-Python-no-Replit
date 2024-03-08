# Escreva um algoritmo que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

salario_mensal = int(input("Digite o salário mensal: "))
horas_mes = int(input("Digite total de horas/mes: "))

valor_hora = salario_mensal / horas_mes

print("O valor/hora é: R$", round(valor_hora, 2))