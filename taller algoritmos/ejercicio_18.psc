Algoritmo ejercicio_18
	escribir "nombres"
	leer nombre 
	escribir"apellido"
	leer apellido
	escribir"segundo apellido"
	leer apellido2
	inicial_nombre<-SubCadena(nombre,1,1)
	inicial_apellido1<-SubCadena(apellido,1,1)
	inicial_apellido2<-SubCadena(apellido2,1,1)
	escribir "iniciales=" mayusculas(inicial_nombre) mayusculas(inicial_apellido1) mayusculas(inicial_apellido2) 
FinAlgoritmo
