#Exibindo as notas que fromarão o dinheiro recebido

notes = int(input())

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


print(notes)
print("{} nota(s) de R$ 100,00".format(notas_100))
print("{} nota(s) de R$ 50,00".format(notas_50))
print("{} nota(s) de R$ 20,00".format(notas_20))
print("{} nota(s) de R$ 10,00".format(notas_10))
print("{} nota(s) de R$ 5,00".format(notas_5))
print("{} nota(s) de R$ 2,00".format(notas_2))
print("{} nota(s) de R$ 1,00".format(resto))