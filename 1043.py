#recebe tres valores verifica se é possivel formar um triangulo
#se for possivel calcular o perimetro
#se nao for calcular a area do trapezio
a,b,c = map(float, input().split())
if (a < b + c) and (b < a + c) and (c < b + a):
	res = "Perimetro = {}".format(a + b + c)
else:
	res = "Area = {}".format(((a + b) * c) / 2)

print(res)		