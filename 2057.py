saida, viajem, time_zone = map(int, input().split())

if saida == 0:
	saida = 24

tempo_viajem = saida + viajem

tempo_viajem += time_zone

if tempo_viajem >= 24:
	tempo_viajem = tempo_viajem - 24

print(tempo_viajem)	