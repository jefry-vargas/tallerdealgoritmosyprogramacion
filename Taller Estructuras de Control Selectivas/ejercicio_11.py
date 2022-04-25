#entradas
Temperatura=int(input("ingrese la temperatura en farenheit "))
#caja negra y salidas
if Temperatura>85:
    print("el deporte apropiado para esta temperatura es natación ")
elif 70<Temperatura<=85:
    print("el deporte apropiado para esta temperatura es tenis")
elif 32<Temperatura<=70:
    print("el deporte apropiado para esta temperatura es golf ")
elif 10<Temperatura<=32:
    print("el deporte apropiado para esta temperatura es esqui ")
elif Temperatura<=10:
    print("el deporte apropiado para esta temperatura es marcha ")