#entradas
X=int(input("ingrese la cantidad de naranjas "))
Y_=int(input("ingrese la cantidad de bolivares por docena "))
K=int(input("ingrese la cantidad de bolivares obtenidos "))
#caja negra
m=(X/12)*Y_
d=(K-m)
g= (d*100)/m
#salidas
print("el porcentaje de ganancia es de: ", g)