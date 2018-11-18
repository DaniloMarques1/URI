estrela = int(input())
roubados = 0
carneiros = list(map(int, input().split()))
flag = 0

while flag < estrela:
	if flag > roubados:
		roubados = flag

	if carneiros[flag] % 2 == 1:
		if carneiros[flag] > 0:
			carneiros[flag] -= 1
		flag += 1
	else:
		if carneiros[flag] > 0:
			carneiros[flag] -= 1
				
		flag -= 1
	if flag < 0:
		break

restante = 0
for i in range(estrela):
	try:
		restante += carneiros[i]
	except:
		break

if estrela > 0:
	roubados += 1

print(carneiros)
print(roubados, restante)