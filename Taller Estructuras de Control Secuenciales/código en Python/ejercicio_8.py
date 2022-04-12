import math
#entradas
a=float(input("escriba el primer lado"))
b=float(input("escriba el segundo lado"))
c=float(input("escriba el tercer lado"))
#caja negra
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
#salidas
print("el area del triangulo es: ", area)