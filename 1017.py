#Quantidade de combustivel gasto em uma viajem em um carro que faz 12km/l
tempo = int(input())
avg = int(input())
distancia = tempo * avg
consumo = distancia / 12
print("{:.3f}".format(consumo))