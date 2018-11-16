
flag = int(input())

for i in range(1,flag + 1):
	x, y = input().split()
	if x == "tesoura" and y == "papel":
		react = "Bazinga!"
	elif x == "papel" and y == "pedra":
		react = "Bazinga!"
	elif x == "pedra" and y == "lagarto":
		react = "Bazinga!"	
	elif x == "lagarto" and y == "Spock":
		react = "Bazinga!"
	elif x == "Spock" and y == "tesoura":
		react = "Bazinga!"
	elif x == "tesoura" and y == "lagarto":
		react = "Bazinga!"
	elif x == "lagarto" and y == "papel":
		react = "Bazinga!"
	elif x == "papel" and y == "Spock":
		react = "Bazinga!"
	elif x == "Spock" and y == "pedra":
		react = "Bazinga!"
	elif x == "pedra" and y == "tesoura":
		react = "Bazinga!"
	elif x == y:
		react = "De novo!"
	else:
		react = "Raj trapaceou!"
	print("Caso #{}: {}".format(i, react))											