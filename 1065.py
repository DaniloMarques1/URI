#Ler 5 numeros e definir quantos sao pares

contador = 0
n1 = int(input())
if n1 % 2 == 0:
	contador += 1
n2 = int(input())
if n2 % 2 == 0:
	contador += 1	
n3 = int(input())
if n3 % 2 == 0:
	contador += 1
n4 = int(input())
if n4 % 2 == 0:
	contador += 1	

n5 = int(input())
if n5 % 2 == 0:
	contador += 1

print("{} valores pares".format(contador))		