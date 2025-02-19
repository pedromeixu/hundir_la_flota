from Barco import Barco
from Tablero import Tablero

if __name__ == "__main__":
    print("Bienvenido a Hundir la Flota")
    tablero = Tablero()

    barco1 = Barco(4, [])
    tablero.agregar_barco_aleatorio(barco1)

    barco2 = Barco(3, [])
    tablero.agregar_barco_aleatorio(barco2)

    print("Este el tablero inicial")
    tablero.mostrar_tablero()

    while not tablero.todos_barcos_hundidos():
        try:

            x = int(input("\nIngresa la coordenada X (0-4):"))
            y = int(input("Ingresa la coordenada Y (0-4):"))

            if 0 <= x < tablero.tamaño and 0 <= y < tablero.tamaño:
                resultado = tablero.recibir_disparo(x, y)
                print(f"El resultado es: {resultado}")
                print("Tablero actualizado")
                tablero.mostrar_tablero()
            else:
                print("Las coordenadas no están en el rango")
        except ValueError:
            print("Introduce números enteros")
    
    print("¡Hundiste la flota!")