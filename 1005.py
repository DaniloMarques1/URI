#Calcular a media entre duas notas recebidas do usuario
#Media ponderada, utilizando pesos

p1 = 3.5
p2 = 7.5
n1 = float(input())
n2 = float(input())
MEDIA = ((n1 * p1) + (n2 * p2)) / (p1 + p2)
print("MEDIA = {:.5f}".format(MEDIA))