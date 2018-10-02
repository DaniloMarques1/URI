h1,m1,hf,mf = map(int,input().split())

h1_minutos = h1 * 60 + m1
hf_minutos = hf * 60 + mf

if hf_minutos > h1_minutos:
	duracao = hf_minutos - h1_minutos
	duracao_horas = duracao // 60
	duracao_minutos = duracao % 60
else:
	h1_minutos = (24 - h1) * 60
	hf_minutos = hf * 60
	duracao = h1_minutos + hf_minutos + (mf - m1)
	duracao_horas = duracao // 60
	duracao_minutos = duracao % 60


print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(duracao_horas,duracao_minutos))