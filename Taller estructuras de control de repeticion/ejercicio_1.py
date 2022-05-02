#entradas
K=int(input("ingrese el valor de K que sea menor a N "))
N=int(input("ingrese el valor de N que sea mayor a K "))
#caja negra
print(N)
while K<N:
    N-=1
    print(N)
    if K==N:
        break