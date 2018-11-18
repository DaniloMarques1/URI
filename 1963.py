p1, p2 = map(float, input().split())
aumento = ((p2 / p1) * 100) - 100
print("{:.2f}%".format(aumento))