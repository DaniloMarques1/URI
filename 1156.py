s = 1
denon = 2
for i in range(3, 40, 2):
	s = s + i / denon
	denon *= 2
print("{:.2f}".format(round(s)))