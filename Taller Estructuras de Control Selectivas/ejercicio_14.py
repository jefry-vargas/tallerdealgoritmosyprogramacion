#entradas
l_anterior=int(input("digite la lectura anterior en kilovatios/hora "))
l_actual=int(input("digite la lectura actual en kilovatios/hora "))
#caja negra
x=l_actual-l_anterior
if x<=100:
    p=4600
elif 100<x<=300:
    p=80000
elif 300<x<=500:
    p=100000
elif x>500:
    p=120000
#salidas
print("el monto(COP/Khw) a pagar es=",p )