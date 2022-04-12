#entradas
ch=int(input("escriba la cantidad en chelines austriacos"))
dg=int(input("digite la cantidad de dracmas griegos "))
pe=int(input("digite la cantidad de pesetas "))
#caja negra
pesetas_ch=(ch*956871)/100
pesetas_dg=(dg*88607)/100
ff_dg=pesetas_dg/20110
do=pe/122499
li=(pe*100)/9289
#salidas
print("la cantidad de chelines austriacos en pesetas es: ", pesetas_ch)
print("la cantidad de dracmas griegos en francos franceses es: ", ff_dg)
print("la cantidad de pesetas en dolares es: ", do)
print("la cantidad de pesetas en liras italianas es: ", li)