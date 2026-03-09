
def hacer_circulo():
    print("Haciendo Circulo")
def hacer_triangulo():
    print("Haciendo Triangulo")
def hacer_rectangulo():
    print("Haciendo Rectangulo")
def hacer_cuadrado():
    print("Haciendo Cuadrado")
def menu():
    print("\nBienvenido a el programa de figuras geometricas\n ")
    print("Selecciona una de las siguientes opciones:\n 1. Circulo\n 2. Triangulo\n 3. Rectagulo\n 4. Cuadrado\n 0. Salir\n")

while True:    
    menu()
    try:
        opcion = int(input("Digita una de las opciones del menu:\n"))
        match opcion:
            case 0:
                print("Saliendo...")
                break
            case 1:
                hacer_circulo()
            case 2:
                hacer_triangulo()
            case 3:
                hacer_rectangulo()
            case 4:
                hacer_cuadrado()
            case _:
                print("Esta opcion no esta en el menu.. Por favor digita una opcion valida")
                continue
    except ValueError:
        print("Entrada Invalida.\n")
