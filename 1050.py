#Exibindo baseado no ddd qual estado esta a ligar

ddd = {61:"Brasilia",71:"Salvador",11:"Sao Paulo",21:"Rio de Janeiro",32:"Juiz de Fora",19:"Campinas",27:"Vitoria",31:"Belo Horizonte"}
value = int(input())
try:
	print(ddd[value])
except:
	print("DDD nao cadastrado")	