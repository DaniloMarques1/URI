salary = float(input())
if salary >= 0 and salary <= 2000:
	print("Isento")
elif (salary >= 2000.01 and salary <= 3000):
	b = salary - 2000
	t = b * 0.08
	print("R$ {:.2f}".format(t))
elif (salary >= 3000.01 and salary <= 4500):
	b = salary - 3000
	t = b * 0.18 + 80
	print("R$ {:.2f}".format(t))
elif (salary > 4500):
	b = salary - 4500
	t = b * 0.28 + 350
	print("R$ {:.2f}".format(t))
