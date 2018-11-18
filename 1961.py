a_pulo, n_canos = map(int, input().split())
canos = list(map(int,input().split()))
for i in range(len(canos) - 1):
	saida = "YOU WIN"
	if abs(canos[i] - canos[i + 1]) > a_pulo:
		saida = "GAME OVER"
		break

print(saida)