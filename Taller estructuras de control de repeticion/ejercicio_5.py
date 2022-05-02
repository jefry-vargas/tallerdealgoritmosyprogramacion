k=1
x=float((k**2+1)/k)
while x<1000:
    k+=1
    x=float(((k**2+1)/k))
    x+=x
    if x<1000:        
        print(k)