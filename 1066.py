#Ler 5 numeros e definir quantos sao pares/impares/positivos/negativos

totImpar = 0
totPar = 0
totPosi = 0
totNega = 0
for i in range(0,5):
	x = int(input())
	if x % 2 == 0:
		totPar += 1
	else:
		totImpar += 1

	if x > 0:
		totPosi += 1
	elif x < 0:
		totNega += 1

print("{} valor(es) par(es)".format(totPar))					
print("{} valor(es) impar(es)".format(totImpar))
print("{} valor(es) positivo(s)".format(totPosi))
print("{} valor(es) negativo(s)".format(totNega))