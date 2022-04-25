#entradas
P=int(input("digite el valor de P"))
Q=int(input("digite el valor de Q"))
#caja negra y salidas
x=(P**3)+(Q**4)-(2*(P**2))
t=(P,Q)
if x>680:
    print(t,"satisfacen la expresión ")
else:
    print(t,"no satisfacen la expresión ")