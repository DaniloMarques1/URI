#Recebendo a quantidade de dias e exibindo em anos:meses:dias

tot_dias = int(input())

anos = tot_dias // 365

resto = tot_dias % 365

meses = resto // 30

dias = resto % 30

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))