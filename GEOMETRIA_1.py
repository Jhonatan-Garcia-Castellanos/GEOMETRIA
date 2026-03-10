import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def hacer_circulo():

    def solicitar_radio(radio):
        area = np.pi * radio**2
        perimetro = 2 * np.pi * radio
        return radio, area, perimetro

    radio = float(input("\n--- Datos del Círculo ---\n  Ingresa el radio del círculo: "))
    r, area, perimetro = solicitar_radio(radio)

    print("Haciendo circulo en 3D:")
    print(f"\nÁrea: {area:.4f}  |  Perímetro: {perimetro:.4f}")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    phi = np.linspace(0, np.pi, 50)
    theta = np.linspace(0, 2*np.pi, 50)

    phi, theta = np.meshgrid(phi, theta)

    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    ax.plot_surface(x, y, z, color='lightblue', edgecolor='black', linewidth=0.5, alpha=0.9)

    ax.set_box_aspect([1,1,1])
    ax.set_xlim([-r*1.2, r*1.2])
    ax.set_ylim([-r*1.2, r*1.2])
    ax.set_zlim([-r*1.2, r*1.2])

    ax.axis('on')
    plt.title(f"Circulo 3D - Radio: {r}\nÁrea: {area:.2f}  |  Perímetro: {perimetro:.2f}")

    plt.show()


def hacer_triangulo():

    def solicitar_datos_triangulo(base, altura, lado_a, lado_b):
        area      = (base * altura) / 2
        perimetro = base + lado_a + lado_b
        return base, altura, area, perimetro

    print("\n--- Datos del Triángulo ---")
    base   = float(input("  Ingresa la base: "))
    altura = float(input("  Ingresa la altura: "))
    lado_a = float(input("  Ingresa el lado a: "))
    lado_b = float(input("  Ingresa el lado b: "))
    base, altura, area, perimetro = solicitar_datos_triangulo(base, altura, lado_a, lado_b)

    print("Haciendo un triángulo:")
    print(f"\nÁrea: {area:.4f}  |  Perímetro: {perimetro:.4f}")

    x = [0, base / 2, base, 0]
    y = [0, altura,   0,    0]

    plt.figure()
    plt.fill(x, y, color="blue", alpha=0.7)
    plt.plot(x, y, color="darkblue", linewidth=2)

    plt.text(base / 2, altura / 3,
             f"Área = {area:.2f}\nPerímetro = {perimetro:.2f}",
             ha='center', va='center', fontsize=11,
             color='white', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='navy', alpha=0.6))

    plt.gca().set_aspect('equal')
    plt.title(f"Triángulo con matplotlib\nÁrea: {area:.2f}  |  Perímetro: {perimetro:.2f}")
    plt.show()


def hacer_rectangulo():

    def solicitar_datos_rectangulo(largo, ancho, altura):
        area      = 2 * (largo*ancho + largo*altura + ancho*altura)
        perimetro = 4 * (largo + ancho + altura)
        return largo, ancho, altura, area, perimetro

    print("\n--- Datos del Rectángulo ---")
    largo  = float(input("  Ingresa el largo (X): "))
    ancho  = float(input("  Ingresa el ancho (Y): "))
    altura = float(input("  Ingresa la altura (Z): "))
    x_len, y_len, z_len, area, perimetro = solicitar_datos_rectangulo(largo, ancho, altura)

    print("Haciendo Rectangulo")
    print(f"\nÁrea Superficial: {area:.4f}  |  Suma de Aristas: {perimetro:.4f}")

    fig = plt.figure(figsize=(10, 8), facecolor='#0d1117')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('white')

    vertices = np.array([
        [0, 0, 0], [x_len, 0, 0], [x_len, y_len, 0], [0, y_len, 0],
        [0, 0, z_len], [x_len, 0, z_len], [x_len, y_len, z_len], [0, y_len, z_len]
    ])

    caras = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[0], vertices[3], vertices[7], vertices[4]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
    ]

    colores = ['#1a3a5c', '#1e4d7a', '#1565c0', '#1976d2', '#1e88e5', '#2196f3']

    poly = Poly3DCollection(caras, facecolors=colores, linewidths=1.5,
                            edgecolors='#64b5f6', alpha=0.85)
    ax.add_collection3d(poly)

    ax.set_xlim([-0.5, x_len + 0.5])
    ax.set_ylim([-0.5, y_len + 0.5])
    ax.set_zlim([-0.5, z_len + 0.5])

    ax.set_xlabel('X', color='#64b5f6', labelpad=10)
    ax.set_ylabel('Y', color='#64b5f6', labelpad=10)
    ax.set_zlabel('Z', color='#64b5f6', labelpad=10)

    ax.text2D(0.05, 0.05,
              f"Área Sup. = {area:.2f}\nAristas   = {perimetro:.2f}",
              transform=ax.transAxes, fontsize=10, color='white',
              bbox=dict(boxstyle='round', facecolor='#1565c0', alpha=0.7))

    ax.set_title('Rectángulo 3D', color="#FFFFFF", fontsize=16, fontweight='bold')
    ax.view_init(elev=25, azim=45)

    plt.tight_layout()
    plt.show()


def hacer_cuadrado():

    def solicitar_datos_cuadrado(lado):
        area      = lado ** 2
        perimetro = 4 * lado
        return lado, area, perimetro

    print("\n--- Datos del Cuadrado ---")
    lado = float(input("  Ingresa el lado del cuadrado: "))
    lado, area, perimetro = solicitar_datos_cuadrado(lado)

    print("Haciendo Cuadrado")
    print(f"\nÁrea: {area:.4f}  |  Perímetro: {perimetro:.4f}")

    x = [0, lado, lado, 0, 0]
    y = [0, 0,    lado, lado, 0]

    plt.figure()
    plt.fill(x, y, color='blue', alpha=0.7)
    plt.plot(x, y, color='darkblue', linewidth=2)

    plt.text(lado / 2, lado / 2,
             f"Área = {area:.2f}\nPerímetro = {perimetro:.2f}",
             ha='center', va='center', fontsize=12,
             color='white', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='navy', alpha=0.6))

    plt.gca().set_aspect('equal')
    plt.title(f"Cuadrado relleno con matplotlib\nÁrea: {area:.2f}  |  Perímetro: {perimetro:.2f}")
    plt.show()


def hacer_rombo():

    def solicitar_datos_rombo(diagonal_mayor, diagonal_menor, altura):
        a = diagonal_mayor / 2
        b = diagonal_menor / 2
        area      = (diagonal_mayor * diagonal_menor) / 2
        perimetro = 4 * np.sqrt(a**2 + b**2)
        return a, b, altura, area, perimetro

    print("\n--- Datos del Rombo ---")
    diagonal_mayor = float(input("  Ingresa la diagonal mayor (d1): "))
    diagonal_menor = float(input("  Ingresa la diagonal menor (d2): "))
    altura         = float(input("  Ingresa la altura de la bipirámide (h): "))
    a, b, h, area, perimetro = solicitar_datos_rombo(diagonal_mayor, diagonal_menor, altura)

    print(f"\nÁrea: {area:.4f}  |  Perímetro: {perimetro:.4f}")

    fig = plt.figure(figsize=(10, 8), facecolor='#0d1117')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor("#ffffff")

    vertices = np.array([
        [ a,  0,  0],
        [ 0,  b,  0],
        [-a,  0,  0],
        [ 0, -b,  0],
        [ 0,  0,  h],
        [ 0,  0, -h],
    ])

    caras = [
        [vertices[0], vertices[1], vertices[4]],
        [vertices[1], vertices[2], vertices[4]],
        [vertices[2], vertices[3], vertices[4]],
        [vertices[3], vertices[0], vertices[4]],
        [vertices[0], vertices[1], vertices[5]],
        [vertices[1], vertices[2], vertices[5]],
        [vertices[2], vertices[3], vertices[5]],
        [vertices[3], vertices[0], vertices[5]],
    ]

    colores = [
        '#6a1b9a', '#7b1fa2', '#8e24aa', '#9c27b0',
        '#ab47bc', '#ba68c8', '#ce93d8', '#e1bee7'
    ]

    poly = Poly3DCollection(caras, facecolors=colores, linewidths=1.5,
                            edgecolors='#e040fb', alpha=0.85)
    ax.add_collection3d(poly)

    ax.set_xlim([-a - 0.5, a + 0.5])
    ax.set_ylim([-b - 0.5, b + 0.5])
    ax.set_zlim([-h - 0.5, h + 0.5])

    for pane in [ax.xaxis.pane, ax.yaxis.pane, ax.zaxis.pane]:
        pane.fill = False
        pane.set_edgecolor('#2d1b4e')

    ax.tick_params(colors='#ce93d8', labelsize=9)
    ax.set_xlabel('X', color='#e040fb', labelpad=10)
    ax.set_ylabel('Y', color='#e040fb', labelpad=10)
    ax.set_zlabel('Z', color='#e040fb', labelpad=10)

    ax.text2D(0.05, 0.05,
              f"Área = {area:.2f}\nPerímetro = {perimetro:.2f}",
              transform=ax.transAxes, fontsize=10, color='white',
              bbox=dict(boxstyle='round', facecolor='#6a1b9a', alpha=0.7))

    ax.set_title('Rombo 3D', color='#f3e5f5', fontsize=16, fontweight='bold')
    ax.view_init(elev=20, azim=45)

    plt.tight_layout()
    plt.show()


def menu():
    print("\nBienvenido a el programa de figuras geometricas\n ")
    print("Selecciona una de las siguientes opciones:\n 1. Circulo\n 2. Triangulo\n 3. Rectangulo\n 4. Cuadrado\n 5. Rombo\n 0. Salir\n")

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
            case 5:
                hacer_rombo()
            case _:
                print("Esta opcion no esta en el menu.. Por favor digita una opcion valida")
                continue
    except ValueError:
        print("Entrada Invalida.\n")