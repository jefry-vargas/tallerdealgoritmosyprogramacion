#entradas
a=int(input("digiet el nivel de hemoglobina en la sangre del paciente "))
b=int(input("digite la edad en meses en caso de sobrepasar los 12 meses, de lo contrario digite 0 "))
c=int(input("digite la edad en años si el paciente tiene mas de 12 meses de edad, de lo contrario, digite 0 "))
d=str(input("digite el sexo del paciente "))
#caja negra
if 0<b<1 and c==0 and 13<=a<=26:
    p=0
if 0<b<=1 and c==0 and 13>a or a>26:
    p=1
if 1<b<=6 and c==0 and 10<=a<=18:
     p=0
if 1<b<=6 and c==0 and 10>a or a>18:
     p=1
if 6<b<=12 and c==0  and 11<=a<=15:
     p=0
if 6<b<=12 and c==0  and 11>a or a>15:
     p=1
if b==0 and 1<c<=5  and 11.5<=a<=15:
     p=0
if b==0 and 1<c<=5  and 11.5>a or a>15:
     p=1
if b==0 and 5<c<=10  and 12.6<=a<=15.5:
     p=0
if b==0 and 5<c<=10  and 12.6>a or a>15.5:
     p=1
if b==0 and 10<c<=15  and 13<=a<=25.5:
     p=0
if b==0 and 10<c<=15  and 13>a or a>15.5:
    p=1
if d=="femenino" and c>15 and 12<a<=16:
    p=0
if d=="femenino" and c>15 and 12>a or a>16:
    p=1 
if d=="masculino" and c>15 and 14<a<=18:
    p=0
if d=="masculino" and c>15 and 14>a or a>18:
    p=1

if p==1:
    print("el paciente tiene anemia")
if p==0:
    print("el paciente no tiene anemia")