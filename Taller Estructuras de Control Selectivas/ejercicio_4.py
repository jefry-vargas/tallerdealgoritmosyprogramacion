#entradas 
piezas=int(input("ingrese la cantidad de piezas="))
costo=int(input("ingrese el valor por pieza"))
#caja negra
total=piezas*costo
if(total>5000000):
    inversion=int(total*.55)
    banco=int(total*.30)
    credito_fabricante=total-inversion-banco
elif(total<5000000):
    inversion=int(total*.70)
    banco=0
    credito_fabricante=int(total*.30)
interes=int(credito_fabricante*.20)
#salidas
print("la inversion de la empresa es de=", inversion)
print("el prestamo del banco es de=", banco)
print("el credito que se le pedira al fabricante es de=", credito_fabricante)
print("el interes por el credito es de=", interes)