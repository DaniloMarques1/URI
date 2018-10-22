#Calculo do salario total tendo o salario bruto e o bonus por itens vendidos

nome = input()
salario_bruto = float(input())
total_vendido = float(input())
salario_total = salario_bruto + (total_vendido * 0.15)
print("TOTAL = R$ {:.2f}".format(salario_total))