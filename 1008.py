#Calculo do salario baseado nas horas trabalhadas e no salario por hora

numero = int(input())
worked = int(input())
per_hour = float(input())
salario = worked * per_hour
print("NUMBER = {}\nSALARY = U$ {:.2f}".format(numero,salario))