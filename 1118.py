while True:
	n1 = float(input())
	while n1 > 10 or n1 < 0:
		print("nota invalida")
		n1 = float(input())

	n2 = float(input())
	while n2 > 10 or n2 < 0:
		print("nota invalida")
		n2 = float(input())
	media = (n1 + n2) / 2 
	print("media = {:.2f}".format(media))
	x = int(input("novo calculo (1-sim 2-nao)\n"))
	while x < 1 or x > 2:
		x = int(input("novo calculo (1-sim 2-nao)\n"))
	if x == 2:
		break