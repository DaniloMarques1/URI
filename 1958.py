valor = float(input())


print(valor)

if valor < 10:
	expoente = 00
else:
	expoente = len(str(valor)) - 1

if valor < 0:
	sinal = "-"
else:
	sinal = "+"			

valor = round(valor,4)
valor = str(valor)
valor = valor.replace(".","")
#parte inteira
x = valor[0]
#parte normalizada
y = valor[1:6]
print("{}{}.{}E{}{:02}".format(sinal,x,y,sinal,expoente))