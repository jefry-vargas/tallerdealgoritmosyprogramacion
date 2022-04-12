#entradas
pago_hora=int(input("Escriba el valor de cada hora "))
horas_extra=int(input("Escriba la cantidad de horas extras"))
hijos=int(input("Escriba la cantidad de hijos"))
hogares=int(input("Escriba la cantidad de hogares"))
actualizaciones=int(input("Digite las actualizaciones academicas"))
horas_dia=int(input("Escriba la cantidad de horas que trabaja al día "))
#caja negra
Aa=actualizaciones*250000
hi=hijos*173000
ho=hogares*180000
asig=Aa+hi+ho
pago_hora_extra=horas_extra*(pago_hora+(pago_hora*.25))
sueldo_b=horas_dia*pago_hora
ded=sueldo_b-(sueldo_b*.14)
sueldo_n=sueldo_b+pago_hora_extra-ded
sn_diciembre=sueldo_n*31
#salidas
print("El valor de las asignaciones es: ", asig)
print("El valor de las deducciones es de: ", ded)
print("El valor del sueldo neto para el mes de diciembre es de: ", sn_diciembre) 