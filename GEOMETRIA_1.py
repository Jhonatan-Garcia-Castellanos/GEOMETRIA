
while True:    
    try:
        print("\nBienvenido a el programa de figuras geometricas\n ")
        opcion = int(input("Selecciona una de las siguientes opciones:\n 1. Circulo\n 2. Triangulo\n 3. Rectagulo\n 4. Rombo\n 5. Cuadrado\n 0. Salir \n"))
        match opcion:
            case 0:
                print("Gracias por usar mi programa adios")
                break
            case 1:
                print("Has elegido el circulo:\n")
            case 2:
                print("Has elegido el triangulo:\n")
            case 3:
                print("Has elegido el rectangulo:\n")
            case 4:
                print("Has elegido el rombo:\n")
            case 5:
                print("Has elegido el cuadrado:\n")
            case _:
                print("Esta opcion no esta en el menu.. Por favor digita una opcion valida")
                break
    except ValueError:
        print("No se puede usar letras digita numero por favor")
