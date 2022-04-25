dep1=int(input("ingrese las ganancias del departamento 1: "))
dep2=int(input("ingrese las ganancias del departamento 2: "))
dep3=int(input("ingrese las ganancias del departamento 3: "))
sueldo=int(input("ingrese el sueldo de los vendedores: "))
#caja negra
total=(dep1+dep2+dep3)*0.33
if dep1>total: 
    x=int(sueldo+sueldo*0.20)
else:
    x=sueldo
if dep2>total: 
    y=int(sueldo+sueldo*0.20)
else:
    y=sueldo
if dep3>total: 
    z=int(sueldo+sueldo*0.20)
else:
    z=sueldo
#salidas
print("el sueldo del vendedor 1 a fin de mes es=: ",x)
print("el sueldo del vendedor 2 a fin de mes es=: ",y)
print("el sueldo del vendedor 3 a fin de mes es=: ",z)