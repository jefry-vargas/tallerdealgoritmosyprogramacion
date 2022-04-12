#entradas
pf=int(input("Ingrese el precio final pagado "))
pvp=int(input("Ingrese el precio de venta al publico"))
#caja negra
descuento=100-((pf*100)/pvp)
#salidas
print("El porcentaje de descuento aplicado es de: ", descuento)