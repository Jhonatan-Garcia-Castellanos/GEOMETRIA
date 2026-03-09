import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def hacer_circulo():
    
    r = float(input("Ingresa el radio del círculo: "))
    print("Haciendo circulo en 3D:")
    
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
    plt.title(f"Circulo 3D - Radio: {r}")

    plt.show()
    # print("Haciendo Circulo")
    # fig, ax = plt.subplots()

    # circulo = Circle((0.5, 0.5),0.2, color='blue', fill=True)

    # ax.add_patch(circulo)

    # ax.set_xlim(0, 1)
    # ax.set_ylim(0, 1)

    # ax.set_aspect('equal')

    # plt.show()

def hacer_triangulo():
    print("Haciendo un trinagulo:")
    print("Haciendo Triangulo")
    x = [0, 1, 2, 0]
    y = [0, 2, 0, 0]

    plt.fill(x, y, color= "blue")

    plt.plot(x, y)

    plt.gca().set_aspect('equal')

    plt.title("Triángulo con matplotlib")

    plt.show()
def hacer_rectangulo():
    print("Haciendo Rectangulo")
    
    fig = plt.figure(figsize=(10, 8), facecolor='#0d1117')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('white')

    x_len, y_len, z_len = 4, 2, 3

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

    ax.set_title('Rectángulo 3D', color="#FFFFFF", fontsize=16, fontweight='bold')
    ax.view_init(elev=25, azim=45)

    plt.tight_layout()
    plt.show()
def hacer_cuadrado():
    print("Haciendo Cuadrado")
    x = [0, 2, 2, 0]
    y = [0, 0, 2, 2]

    plt.fill(x, y, color='blue')

    plt.gca().set_aspect('equal')

    plt.title("Cuadrado relleno con matplotlib")

    plt.show()
def hacer_rombo():
    fig = plt.figure(figsize=(10, 8), facecolor='#0d1117')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor("#ffffff")

    a = 2  
    b = 1  
    h = 3  

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
