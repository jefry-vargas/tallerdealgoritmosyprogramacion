#entradas
bx=int(input("Digite la cantidad de Bolivares prestados"))
by=int(input("Digite la cantidad de Bolivares que se pagaron con un interes de 4 años"))
#caja negra
b=(by*100)/(bx*4)
#salidas
print("el porcentaje que se cobraron por el prestamo fue: ", b)