#Exibindo a quantidade de notas e moedas que formam um dinheiro recebido
notes = float(input())


#Notas
notas_100 = notes // 100
resto = notes % 100

notas_50 = resto // 50
resto = resto % 50

notas_20 = resto // 20
resto = resto % 20

notas_10 = resto // 10
resto = resto % 10

notas_5 = resto // 5
resto = resto % 5

notas_2 = resto // 2
resto = resto % 2

decimal = round(resto * 100)

#Moedas
moedas_1 = decimal // 100
resto = decimal % 100

moedas_05 = resto // 50
resto = resto % 50

moedas_025 = resto // 25
resto = resto % 25

moedas_010 = resto // 10
resto = resto % 10

moedas_005 = resto // 5
resto = resto % 5

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(notas_100)))
print("{} nota(s) de R$ 50.00".format(int(notas_50)))
print("{} nota(s) de R$ 20.00".format(int(notas_20)))
print("{} nota(s) de R$ 10.00".format(int(notas_10)))
print("{} nota(s) de R$ 5.00".format(int(notas_5)))
print("{} nota(s) de R$ 2.00".format(int(notas_2)))

print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(moedas_1))
print("{} moeda(s) de R$ 0.50".format(moedas_05))
print("{} moeda(s) de R$ 0.25".format(moedas_025))
print("{} moeda(s) de R$ 0.10".format(moedas_010))
print("{} moeda(s) de R$ 0.05".format(moedas_005))
print("{} moeda(s) de R$ 0.01".format(resto))

