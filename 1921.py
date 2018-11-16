lados = int(input())
flag = 0
contador = 0
for i in range(0, 1):
	for j in range(i + 2, lados):
		flag += 1
contador += flag

for i in range(1,lados):
	flag -= 1
	contador += flag


print(contador)