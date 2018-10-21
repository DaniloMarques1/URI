d = {"C":0,"S":0,"R":0}
flag = int(input())
while flag > 0:
	qtd, animal = input().split()
	qtd = int(qtd)
	d[animal] += qtd
	flag -= 1
total = d["C"] + d["R"] + d["S"]
percentC = (d["C"] / total) * 100
percentR = (d["R"] / total) * 100
percentS = (d["S"] / total) * 100 
print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(d["C"]))
print("Total de ratos: {}".format(d["R"]))
print("Total de sapos: {}".format(d["S"]))
print("Percentual de coelhos: {:.2f} %".format(percentC))
print("Percentual de ratos: {:.2f} %".format(percentR))
print("Percentual de sapos: {:.2f} %".format(percentS))	
	