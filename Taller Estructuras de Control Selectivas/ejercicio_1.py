#entradas
a=int(input("digite la cantidad invertida"))
b=float(input("digite la tasa de interes"))
#caja negra
i=int(a*b)
t=int(a+i)
#salidas
if(i>100000):
    print("la cantidad generada es de=", i)
    print("supera los 100000")
else:
    print("la cantidad generada es de=", i)
    print("no superan los 100000")
print("el saldo total que se encuentra en la cuenta es de", t)