while True:
	try:
		#pegando os slugs ate o EOF
		numbersSlug = int(input())
		slugs = map(int, input().split())
	except:
		#caso nada seja digitado no input, quebrar o loop
		break
	else:
		#definindo o nivel de velocidade
		speed = max(slugs)
		if speed <= 10:
			print("1")
		elif speed < 20:
			print("2")
		elif speed >= 20:
			print("3")		

