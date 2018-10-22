#Troca de cartas
#A quantidade de troca de cartas ocorre atraves do maior divisor comum
test = int(input())
for i in range(0,test):
	x,y = map(int,input().split())
	if x > y:
		maior = x
		menor = y
	else:
		maior = y
		menor = x

	while maior % menor != 0:
		maior, menor = menor, maior % menor
	print(menor)
