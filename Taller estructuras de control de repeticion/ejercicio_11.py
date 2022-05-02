z=int(input("ingrese el numero de personas encuestadas "))
i=int(0)
lista_si=[]
lista_no=[]
lista_aguardiente=[]
lista_ron=[]
lista_cerveza=[]
lista_tequila=[]
lista_whisky=[]
lista_otro=[]
lista_masculino=[]
lista_femenino=[]
lista_menores_edad_F=[]
lista_hombres_ag=[]
lista_edades_c=[]
while i<z:
    i+=int(1)
    a=str(input("¿consume licor? "))
    b=str(input("su licor preferido "))#si responde no a la anterior pregunta,aqui va "no tiene"
    c=int(input("su edad "))
    d=str(input("su sexo "))
    if a=="si":
        lista_si.append(a)
    if a=="no":    
        lista_no.append(a)
    if b=="aguardiente":
        lista_aguardiente.append(b)
    if b=="ron":
        lista_ron.append(b)
    if b=="cerveza":
        lista_cerveza.append(b)
        lista_edades_c.append(c)
    if b=="tequila":
        lista_tequila.append(b)
    if b=="whisky":
        lista_whisky.append(b)
    if b=="otro":
        lista_otro.append(b)
    if b=="masculino":
        lista_masculino.append(d)
    if b=="femenino":
        lista_femenino.append(d)
    if d=="femenino" and c<18:
        lista_menores_edad_F.append(c)
    if d=="masculino" and b!="aguardiente" and 20<c<25:
        lista_hombres_ag.append(c)
    if i==z:
        break
Pwhisky=(len(lista_whisky)*100)/z
Q=sum(lista_edades_c)
W=len(lista_cerveza)
pro_cerv=float(Q/W)
print(" total de personas que consumen licor es de= ",len(lista_si))    
print(" total de mujeres menores de edad es de= ",len(lista_menores_edad_F))
print(" total de hombres que no consumen aguardiente y que tienen entre 20 y 25 es de= ", len(lista_hombres_ag))
print(" promedio de edades de las personas que consumen cerveza es de= ",pro_cerv)
print(" porcentaje de personas que consumen wisky en relacion con el total encuestado es de= ",Pwhisky)
    