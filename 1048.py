#Reajuste no salario baseado no salario

salario = float(input())

if salario <= 400:
	reaj = 0.15
elif salario <= 800:
	reaj = 0.12
elif salario <= 1200:
	reaj = 0.1
elif salario <= 2000:
	reaj = 0.07
else:
	reaj = 0.04

novo_salario = salario + (reaj * salario)
aumento = novo_salario - salario

print("Novo salario: {:.2f}".format(novo_salario) )
print("Reajuste ganho: {:.2f}".format(aumento))
print("Em percentual: {} %".format(int(reaj * 100)))			