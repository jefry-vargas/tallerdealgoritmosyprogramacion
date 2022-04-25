#entradas
km=int(input("ingrese la cantidad de km recorridos"))
#caja negra
if km<300:
    b=50000
if 300<km<1000:
    b=70000+(km-300)+30000
if km>=1000:
    b=150000+(km-300)*9000
#salidas
print("el valor a pagar por el cliente es de: ",b)