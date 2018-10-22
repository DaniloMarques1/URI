size = int(input())
l = [int(x) for x in input().split()]
menor = float("inf")
for i in range(0, size):
	if l[i] < menor:
		menor = l[i]
		pos = i
print("Menor valor: {}".format(menor))
print("Posicao: {}".format(pos))		