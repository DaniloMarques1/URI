t1,tf = map(int, input().split())
if t1 >= tf:
	duracao = (24 - t1) + tf
else:
	duracao = tf - t1
print("O JOGO DUROU {} HORA(S)".format(duracao))