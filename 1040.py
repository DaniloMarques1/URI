values = input().split()
n1,n2,n3,n4 = values

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

p1 = 2
p2 = 3
p3 = 4
p4 = 1

media = ((n1 * p1) + (n2 * p2) + (n3 * p3) + (n4 * p4)) / (p1 + p2 + p3 + p4)
print("Media: {:.1f}".format(media))

if media > 7:
	print("Aluno aprovado.")
elif media >= 5:
	print("Aluno em exame.")
	nota_exame = float(input())
	print("Nota do exame: {:.1f}".format(nota_exame))
	if nota_exame >= 5:
		media_final = (media + nota_exame) / 2
		print("Aluno aprovado.")
		print("Media final: {:.1f}".format(media_final))
	else:
		print("Aluno reprovado.")
else:
	print("Aluno reprovado.")
