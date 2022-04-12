#entradas
sueldo_base=int(input("ingrese el sueldo base"))
venta_1=int(input("ingrese el valor de la primera venta"))
venta_2=int(input("ingrese el valor de la segunda venta"))
venta_3=int(input("ingrese el valor de la tercera venta"))
#caja negra
comisiones=int((venta_1+venta_2+venta_3)*.10)
sueldo_total=int(comisiones+sueldo_base)
#salidas
print("las comisiones son: ", comisiones)
print("el total recibido es: ", sueldo_total)