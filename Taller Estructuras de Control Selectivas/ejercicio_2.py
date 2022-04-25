#entradas
sueldo = float (input ('Ingresa el valor de sueldo: '))
#caja negra
if sueldo<900000:
    aumento=float(sueldo*.15)
else:
    aumento=float(sueldo*.12)
nuevo_sueldo=int(sueldo+aumento)
#salidas
print ("Valor del nuevo sueldo=", nuevo_sueldo)