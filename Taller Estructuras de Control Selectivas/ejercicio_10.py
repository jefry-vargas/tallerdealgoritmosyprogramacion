#entradas
a=int(input("ingrese el sueldo bruto del trabajador "))
b=input("ingrese la categoria del trabajador")
#caja negra
if(b==1) and (a>=5000000):
    salario=int(a+(a*.10))
elif(b==2) and (3600000<a<=4300000):
    Salario=int(a+(a*.15))
elif (b==3) and (2000000<a<=3600000):
    Salario=int(a+(a*.20))
elif (b==4) and (900000<a<=2000000):
    Salario=int(a+(a*.40))
elif (b==5) and (a<=900000):
    Salario=int(a+(a*.60))
# salidas
print("el nuevo sueldo bruto del trabajador es de:", salario)
print("la categoria del trabajador es de: ", b)