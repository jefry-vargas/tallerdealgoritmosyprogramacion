#entradas
from cmath import sqrt
A=int(input("ingrese valor de A "))
B=int(input("ingrese valor de B "))
C=int(input("ingrese valor de C "))
#caja negra
D=(B**2)-4*A*C
if D==0:
    r=-B/(2*A)
    print("el valor de X2 y X1 es=", r)
elif D>0:
    X1=(-B + sqrt(B**2-4*A*C))/(2*A)
    X2=(-B - sqrt(B**2-4*A*C))/(2*A)
    print("X1 es igual a: ", X1)
    print("X2 es igual a: ", X2)
elif D<0:
    print("no tiene solucion en los reales")