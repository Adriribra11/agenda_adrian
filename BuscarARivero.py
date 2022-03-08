#Al iniciar el programa se muestra el menú.
#Seleccionamos la opción deseada. En mi caso la 2, buscar.
#Pregunta a quien quieres buscar.
#Si lo encuentra lo muestra. Si no dice que el contacto no existe y que lo agregemos desde el menú

def agenda():
    print ("#---------------------------------#")
    print ("#              Menú               #")
    print ("#---------------------------------#")
    print ("#    1.-  Añadir/modificar        #")
    print ("#    2.-  Buscar                  #")
    print ("#    3.-  Borrar                  #")
    print ("#    4.-  Listar                  #")
    print ("#---------------------------------#")

def buscar_ARivero():  
    buscar=input("¿Qué contacto buscas?: ")
    print (contactos[buscar])
    time.sleep(3)
    os.system("clear")
    if buscar not in contactos:
       print("El contacto no existe, agregualo desde el menú")
agenda()
option =int(input("Elige la opción que quieras: "))
while option == 2 :
    buscar_ARivero()