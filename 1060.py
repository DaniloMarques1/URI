#Ler 6 numeros e definir quantos sao positivos
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())
numbers = [n1,n2,n3,n4,n5,n6]
totPositive = 0
for i in numbers:
	if i > 0:
		totPositive += 1
print("{} valores positivos".format(totPositive))