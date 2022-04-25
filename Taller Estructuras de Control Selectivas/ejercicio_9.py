#entradas
nombre_cliente=str(input("ingrese su nombre"))
compra=int(input("digite cantidad del monto de la compra "))
#caja negra
if compra<50000:
    total=compra
    descuento=0
if compra>=50000 and compra<100000:
    total=compra-(compra*0.05)
    descuento=5
elif compra>=100000 and compra<700000:
    total=compra-(compra*0.11)
    descuento=11
elif compra>=700000 and compra<1500000:
    total=compra-(compra*0.18)
    descuento=18
elif compra>1500000:
    total=compra-(compra*0.25)
    descuento=25
#salidas
print(nombre_cliente)
print("el monto de la compra es=: ",compra)
print("el monto a pagar es=: ",total )
print("el descuento recibido es=: ",descuento )