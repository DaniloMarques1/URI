totGasolina = 0
totDiesel = 0
totAlcool = 0

flag = int(input())
while flag != 4:
	if flag == 1:
		totAlcool += 1
	elif flag == 2:
		totGasolina += 1	
	elif flag == 3:
		totDiesel += 1
	flag = int(input())
print("MUITO OBRIGADO")
print("Alcool: {}".format(totAlcool))
print("Gasolina: {}".format(totGasolina))
print("Diesel: {}".format(totDiesel))			