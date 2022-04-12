#entradas
#matematicas
examen_m=float(input("ingrese la nota del examen de matematicas:"))
tarea1_m=float(input("ingrese la nota del tarea 1:"))
tarea2_m=float(input("ingrese la nota del tarea 2:"))
tarea3_m=float(input("ingrese la nota del tarea 3:"))
#fisica
examen_f=float(input("ingrese la nota del examen de fisica:"))
tarea1_f=float(input("ingrese la nota del tarea 1:"))
tarea2_f=float(input("ingrese la nota del tarea 2:"))
#quimica
examen_q=float(input("ingrese la nota del examen de quimica:"))
tarea1_q=float(input("ingrese la nota del tarea 1:"))
tarea2_q=float(input("ingrese la nota del tarea 2:"))
tarea3_q=float(input("ingrese la nota del tarea 3:"))
#caja negra
promedio_m=examen_m*.90 + ((tarea1_m + tarea2_m + tarea3_m)/3)*.10
promedio_f=examen_f*.80 + ((tarea1_f + tarea2_f)/2)*0.20
promedio_q=examen_q*.85 + ((tarea1_q + tarea2_q + tarea3_q)/3)*.15
promedio_general=((promedio_m+promedio_f+promedio_q)/3)
#salida
print("el promedio general de las tres materias es:", promedio_general)
print("el promedio de matematicas es: ", promedio_m)
print("el promedio de fisica es: ", promedio_f)
print("el promedio de quimica es: ", promedio_q)