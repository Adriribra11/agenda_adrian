#autor: Adrian Rivero Bravo
#fecha de modificación: 10-03-2022
#Pregunta a quien quieres buscar.
#Si lo encuentra lo muestra. Si no dice que el contacto no existe y que lo agregemos desde el menú

def buscar_ARivero(nombre, agenda):  
    #Te aparece un mensaje y pide que digas que contacto buscas.
    buscar=input("¿Qué contacto buscas?: ") 
    #Si existe el contacto aparecerá su información
    print (contactos[buscar])
    time.sleep(3)
    os.system("clear")
    #Si no existe el contacto, aparecerá el siguiente mensaje.
    if buscar not in contactos:
       print("El contacto no existe, agregualo desde el menú")
