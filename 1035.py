#Lê 4 valores e verifica se são aceitos ou não de acordo com algumas condições

values = input().split()
a,b,c,d = values
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if ((b>c) and (d > a)) and ((c + d) > (b + a)) and (c > 0 and d > 0) and a % 2 == 0:
	print("Valores aceitos")
else:
	print("Valores nao aceitos")	
