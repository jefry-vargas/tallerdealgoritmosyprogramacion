#entradas
parcial1=int(input("digite calificacion parcial 1 "))
parcial2=int(input("digite calificacion parcial 2 "))
parcial3=int(input("digite calificacion parcila 3 "))
examen_final=int(input("digite calificacion del examen final "))
proyecto_final=int(input("digite calificacion proyecto final "))
#caja negra
promedio_parciales=(parcial1+parcial2+parcial3)/3
calificacion_total=((promedio_parciales*.55)+(examen_final*.3)+(proyecto_final*.15))
#salidas
print("la calificacion total en computación es: ", calificacion_total)