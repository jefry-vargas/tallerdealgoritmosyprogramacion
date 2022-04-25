#entradas
A=int(input("ingrese el valor de A"))
B=int(input("ingrese el valor de B"))
C=int(input("ingrese el valor de C"))
D=int(input("ingrese el valor de D"))
#salidas 
if(D==0):
    R=((A-C)**2)
    print("la formula ((A-C)**2) es igual a= ", R)
elif(D>0):
    M=(((A-B)**3)/D)
    print("la formula de (((A-B)**3)/D) es igual a= ", M)
else:
    print("no hay formula para ese número ")