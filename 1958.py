valor = float(input())
sinal_numero = "+"

#qual sinal o numero vai ter
if valor < 0:
	sinal_numero = "-"				
valor = abs(valor)

if valor < 10:
	expoente = 00
else:
	#length do numero menos a parte inteira o ponto e 0 zero do flutuante
	expoente = len(str(valor)) - 3
if valor > 0 and valor < 1:
	sinal_expoente = "-"
else:
	sinal_expoente = "+"


valor = str(valor)
valor = valor.replace(".","")
#parte inteira
x = valor[0]
#parte normalizada
y = valor[1:5]
juntar = float(x + y)
print(juntar)
print("{}{}.{}E{}{:02}".format(sinal_numero,x,y,sinal_expoente,expoente))