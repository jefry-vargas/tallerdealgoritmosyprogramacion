#entradas
a=int(input("ingrese el dia de su nacimiento "))
b=int(input("ingrese el mes de su nacimiento "))
c=int(input("ingrese el año de su nacimiento "))
d=int(input("ingrese el dia actual "))
e=int(input("ingrese el mes actual "))
f=int(input("ingrese el año actual "))
#caja negra y salidas
if b==11 and a>=22 and a<=30 or b==12 and a<=21:
    print("sagitario") 
if b==12 and a>=22 or b==1 and a<=20:
    print("capricornio")
if b==1 and a>=21 or b==2 and a<=19:
    print("acuario")
if b==2 and a>=20 or b==3 and a<=19:
    print("piscis")
if b==3 and a>=21 or b==4 and a<=20:
    print("aries")
if b==4 and a>=21 or b==5 and a<=21:
    print("tauro")
if b==5 and a>=22 or b==6 and a<=21:
    print("geminis")
if b==6 and a>=22 or b==7 and a<=22:
    print("cancer")
if b==7 and a>=23 or b==8 and a<=23:
    print("leo")
if b==8 and a>=24 or b==9 and a<=22:
    print("virgo")
if b==9 and a>=23 or b==10 and a<=22:
    print("libra")
if b==10 and a>=23 or b==11 and a<=21:
    print("escorpion")
if  b>e:
    edad=(f-c)-1
else:
    edad=(f-c)
print("la edad del usuario es de: ",edad)