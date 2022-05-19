usuarios ={
    "iperurena":{
        "nombre": "Iñaki",
            "apellido": "Perurena",
            "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
    },
}
for x in range(1,4,1):
    User = input("usuario: ")
    Pass = input("contraseña: ")
    if User in usuarios and Pass == usuarios[User]['password']:
        a=usuarios[User]["nombre"]
        b=usuarios[User]["apellido"]
        print(a)
        print(b)
        break
    if x==3:
        print("se acabaron los intentos")
        break
    else:
        print("intentelo denuevo")
    
    

            

