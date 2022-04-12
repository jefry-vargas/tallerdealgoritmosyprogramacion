#entradas
hombres=int(input("cantidad hombres: "))
mujeres=int(input("cantidad de mujeres: "))
#caja negra
total=mujeres+hombres
porcentaje_M=round((mujeres/total)*100)
porcentaje_H=round((hombres/total)*100)
#salidas
print("El porcentaje de mujeres es:", porcentaje_M )
print("El porcentaje de hombres es: ", porcentaje_H) 