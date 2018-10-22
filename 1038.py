#Recebendo o codgo do produto e a quantidade e retornando o preço

products = {"1":4.00,"2":4.50,"3":5.00,"4":2.00,"5":1.5}

values = input().split()
x,y = values


#quantidade do produto
y = int(y)

total = products[x] * y
 
print("Total: R$ {:.2f}".format(total))