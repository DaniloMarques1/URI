#Duração de um jogo recebendo a hora inicial e a hora final o jogo podendo terminar no dia seguinte

t1,tf = map(int, input().split())
if t1 >= tf:
	duracao = (24 - t1) + tf
else:
	duracao = tf - t1
print("O JOGO DUROU {} HORA(S)".format(duracao))