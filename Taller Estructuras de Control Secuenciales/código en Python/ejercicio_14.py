#entradas
ck=int(input("Ingrese el Costo por kilovateo"))
lan=int(input("Ingres la Lectura anterior "))
lac=int(input("Ingrese la Lectura actual"))
#caja negra
monto_total=(lac-lan)*ck
#salidas
print("el monto total a pagar es de: ", monto_total)