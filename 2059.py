p, j1, j2, c, a = map(int, input().split())

if (j1 + j2) % 2 == 0:
	if p == 0:
		if c == 1 and a == 0:
			vencedor = "Jogador 1 ganha!"
		elif c == 0 and a == 1:
			vencedor = "Jogador 1 ganha!"
		else:
			vencedor = "Jogador 2 ganha!"
	else:
		if c == 1 and a == 1:
			vencedor = "Jogador 2 ganha!"
		else:
			vencedor = "Jogador 1 ganha!"
else:
	if p == 1:
		if c == 1 and a == 0:
			vencedor = "Jogador 1 ganha!"
		elif c == 0 and a == 1:
			vencedor = "Jogador 1 ganha!"
		else:
			vencedor = "Jogador 2 ganha!"
	else:
		if c == 1 and a == 1:
			vencedor = "Jogador 2 ganha!"
		else:
			vencedor = "Jogador 1 ganha!"						
print(vencedor)						