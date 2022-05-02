d=0
e=0
f=0
while(True):
    a=int(input())
    if(a == 4):
        break
    else:
        if (a == 1):
            d +=1
        elif (a == 2):
            e+=1
        elif (a == 3):
            f+=1
        else:
            continue
print("MUITO OBRIGADO")
print("Alcool:",d)
print("Gasolina:",e)
print("Diesel:",f)