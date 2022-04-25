#entradas
b=int(input("Ingresa la cantidad entera de dinero en COP:"))
#caja negra
c1=(b-b%100000)//100000
b=b%100000
c2=(b-b%50000)//50000
b=b%50000
c3=(b-b%20000)//20000
b=b%20000
c4=(b-b%10000)//10000
b=b%10000
c5=(b-b%5000)//5000
b=b%5000
c6=(b-b%2000)//2000
b=b%2000
c7=(b-b%1000)//1000
b=b%1000
c8=(b-b%500)//500
b=b%500
c9=(b-b%200)//200
b=b%200
c10=(b-b%100)//100
b=b%100
c11=(b-b%50)//50
#salidas
print(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11)