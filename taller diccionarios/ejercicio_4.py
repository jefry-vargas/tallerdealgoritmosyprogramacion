x=int(input("número de estudiantes "))
a=[]
b=[]
c=[]
d={}
for c in range(1,x+1,1):
    e=input("nombre estudiante ")
    f=float(input("nota estudiante "))
    d.update({c:{"nombre":e, "nota":f}})
for i in d.keys():
    if (d[i]["nota"])<=5:
            b.append(d[i]["nombre"])
    if (d[i]["nota"])>5:
        a.append(d[i]["nombre"])
    c.append(d[i]["nota"])
m=(sum(c))/x
print("estudiante/s suspendio/s= ",b)
print("estudiante/s aprobado/s= ",a)
print("promedio: ",m)