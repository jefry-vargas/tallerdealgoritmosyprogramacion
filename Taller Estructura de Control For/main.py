archivo = open('paises.txt', 'r')
#imprima la posicion de colombia
"""
c=0
lista=[]
for i in archivo:
  lista.append(i)
  a=" ".join(lista)
  c=c+1 
  if(a=="Colombia: Bogotá\n"):
    break
  lista=[]   
print(c)
"""
#Imprima todos los paises
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""
#Imprima todas las Capitales
"""
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)):
    lista.append(i[r])
  a="".join(lista)
  print(a)
  lista=[]
"""  
#Imprimir todos los paises que inicien con la letra C
"""
lista=[]
paises=[]
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  paises.append(a)
  lista=[]
for i in paises:
  if(i[0]=="C"):
    print(i)
"""  
#imprima todas las capitales que inicien con la leta B
"""
lista=[]
ciudad=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudad:
  if(i[0]=="B"):
    print(i)  
"""
#Cuente e imprima cuantas ciudades inician con la latra M  
"""
c=0
ciudad=[]
lista=[]
for i in archivo:
  a=i.index(":")
  for r in range(a+2,len(i)-1):
    lista.append(i[r])
  a="".join(lista)
  ciudad.append(a)
  lista=[]
for i in ciudades:
  if(i[0]=="M"):
    c=c+1
    print(i)
print(c)
"""
#Imprima todos los paises y capitales, cuyo inicio sea con la letra U
"""
for i in archivo:
  a,b=i.split(": ")
  a=str(a)
  b=str(b)
  if x[0]=="U":
    print(a)
  if y[0]=="U":
    print(b)
"""
#Cuente e imprima cuantos paises que hay en el archivo
"""
lista=[]
c=0
for i in archivo:
  a=i.index(":")
  c+=1
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  lista=[]
print(c)
"""
#Busque e imprima la ciudad de Singapur
"""
for i in archivo:
  a,y=i.split(": ")
  a=str(a)
  b=str(b)
  if a!="Singapur":
    pass
  else:
    print(b)
"""
#Busque e imprima el pais de Venezuela y su capital
"""
for i in archivo:
  a,b=i.split(": ")
  a=str(a)
  b=str(b)
  if a!="Venezuela":
    pass
  else:
    print(a)
    print(b)
"""
#Cuente e imprima las ciudades que su pais inicie con la letra E
"""
ciudad=[]
c=0
for i in archivo:
  a,b=i.split(": ")
  a=str(a)
  b=str(b)
  if a[0]!="E":
    pass
  else:
    ciudad.append(b)
    print(a)
    print (b)
print(len(ciudad))
"""
#Buesque e imprima la Capiltal de Colombia
"""
for i in archivo:
  a,y=i.split(": ")
  a=str(a)
  b=str(b)
  if a!="Colombia":
    pass
  else:
    print(b)
"""
#imprima la posicion del pais de Uganda
"""
lista=[]
c=1
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  lista=[]
  if a!="Uganda":
    c+=1
  if a=="Uganda":
    break
print (c)
"""
#imprima la posicion del pais de Mexico
"""
lista=[]
c=1
for i in archivo:
  a=i.index(":")
  for r in range(0,a):
    lista.append(i[r])
  a="".join(lista)
  lista=[]
  if a!="México":
    c+=1
  if a=="México":
    break
print (c)
"""
#El alcalde de Antananarivo contrato a algunos alumnos de la Universidad Ean para corregir el archivo de países.txt, ya que la capital de Madagascar NO es rey julien es Antananarivo, espero que el alcalde se vaya contento por su trabajo. Utilice un For para cambiar ese Dato
""""
pais=[]
for i in archivo:
  pais.append(i)
  if i=="Madagascar: rey julien\n":
    x=pais.index("Madagascar: rey julien\n")
    pais.remove("Madagascar: rey julien\n")
    pais.insert(x,"Madagascar: Antananarivo\n")
  a="".join(pais)
  print(a)
  pais=[]
"""
#Agregue un país que no esté en la lista 
"""
pais = "Palestina: Jerusalén"
pais_n=open("paises.txt","a")
pais_n.write("\n"+pais+"\n")
pais_n.close()
"""

archivo.close()
