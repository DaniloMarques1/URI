import math
point1 = input().split()
point2 = input().split()

x1, y1 = point1
x2,y2 = point2

x1 = float(x1)
x2 = float(x2)
y1 = float(y1)
y2 = float(y2)

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("{:.4f}".format(distance))