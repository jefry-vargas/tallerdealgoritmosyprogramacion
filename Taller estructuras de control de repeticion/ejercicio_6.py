x, y=input().split(" ")
x=int(x)
y=int(y)
z=x-y
lista=[z]
while z>0:
    z-=y
    lista.append(z)
print("el resto de la divisiones de=",z)
print("canditad de restas realizadas=",len(lista))