values = input().split()
pi = 3.14159
area_tri = (float(values[0]) * float(values[2])) / 2
area_circulo = float(values[2]) ** 2 * pi
area_trape = ((float(values[0]) + float(values[1])) * float(values[2])) / 2
area_quad = float(values[1]) ** 2
area_ret = float(values[0]) * float(values[1])

print("TRIANGULO: {:.3f}".format(area_tri))
print("CIRCULO: {:.3f}".format(area_circulo))
print("TRAPEZIO: {:.3f}".format(area_trape))
print("QUADRADO: {:.3f}".format(area_quad))
print("RETANGULO: {:.3f}".format(area_ret))