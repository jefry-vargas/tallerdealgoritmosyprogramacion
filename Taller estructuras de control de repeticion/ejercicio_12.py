#Puntaje Alto
punta_alto = 0
nombre_alto = ""
#Puntaje Bajo
punta_bajo = 0
nombre_bajo = ""
#Promedio Puntaje
puntajep = 0
#Inferior al promedio
inf = []
#Superior al promedio
sup = []
num_estudiantes=int(input("Ingresa la cantidad de estudiantes: "))
for i in range(0,num_estudiantes):
   nombre, puntaje= input().split(" ")
   nombre=str(nombre)
   puntaje=int(puntaje)
   puntajep = puntajep + puntaje
   punta_prom = puntajep/num_estudiantes
#Puntaje más alto
if(puntaje > punta_alto):
   punta_alto=puntaje
   nombre_alto=nombre
#Puntaje más bajo
if(puntaje < punta_alto or puntaje<punta_bajo):
    punta_bajo = puntaje
    nombre_bajo = nombre
#Inferior al promedio
if(puntaje < punta_prom):
    inf.append(puntaje)
#Superior al promedio
if(puntaje > punta_prom):
   sup.append(puntaje)
#Inf al promedio
pinf = (len(inf)*100)/num_estudiantes
#Sup al promedio
psup = (len(sup)*100)/num_estudiantes
print(f"El estudiante con el puntaje más alto es: {nombre_alto}")
print(f"El estudiante con el puntaje más bajo es: {nombre_bajo}")
print(f"El puntaje maximo obtenido es: {punta_alto}")
print(f"El puntaje minimo obtenido es: {punta_bajo}")
print("El promedio del puntaje es:",("{0:.2f}".format(punta_prom)))
print("El porcentaje de estudiantes con puntajes inferiores al promedio es:",("{0:.0f}".format(pinf)+str("%")))
print("El porcentaje de estudiantes con puntajes superiores al promedio es:",("{0:.0f}".format(psup)+str("%")))