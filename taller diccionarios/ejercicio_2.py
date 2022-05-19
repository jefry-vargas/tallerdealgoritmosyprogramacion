ejemplo={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,'Maite': 5}
lista=[]
for i in ejemplo:
    lista.append(ejemplo[i])
    coleccion=set(lista)
print(coleccion)