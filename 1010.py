#Ler o codigo do produto, a quantidade e o preço duas vezes e depois calcula o total a pagar


product1 = input()
product1 = product1.split(" ")
product2 = input()
product2 = product2.split(" ")
total_product_1 = float(product1[1]) * float(product1[2])
total_product_2 = float(product2[1]) * float(product2[2])
total = total_product_1 + total_product_2
print("VALOR A PAGAR: R$ {:.2f}".format(total))