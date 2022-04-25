#entradas
A=int(input("ingrese un valor para A "))
B=int(input("ingrese un valor para B "))
C=int(input("ingrese un valor para C "))
D=int(input("ingrese un valor para D "))
#caja negra 
t=(A*1000)+(B*100)
r=(C*10)+D
if r>=60:
    z=t+100
else:
    z=int(t)
#salidas
print("el entero positivo N redondeado es: ",z)