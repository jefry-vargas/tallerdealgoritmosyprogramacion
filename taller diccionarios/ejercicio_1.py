ejm=[12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64,23]
resultado={}
coleccion=set(ejm)
for x in coleccion:
    diccionario={
        x:ejm.count(x)   
    }
    resultado.update(diccionario)
print(resultado)
