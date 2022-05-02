e=int(input("ingrese la cantidad de estudiantes "))
c=0
lista=[]
while c<e:
    c+=1
    a=float(input("ingrese su estatura "))
    lista.append(float(a))
    if c==e:
        r=max(lista,key=float)
        print("la estatura mayor es de: ",r)