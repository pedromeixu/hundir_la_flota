from Barco import Barco
from Tablero import Tablero
import random

if __name__ == "__main__":

    tablero = Tablero()

    def generar_coordenadas_barco(tamaño, x, y, direccion):
        coordenadas = []

        if direccion == "horizontal":
            for i in range(tamaño):
                coordenadas.append((x + i, y))
        else:
            for i in range(tamaño):
                coordenadas.append((x, y + i))
        
        return coordenadas
    
    x1, y1 = random.randint(0, tablero.tamaño -1), random.randint(0, tablero.tamaño - 1)
    direccion1 = random.choice ( ["horizontal", "vertical"] )
    barco1 = Barco(3, generar_coordenadas_barco(3, x1, y1, direccion1))
    
    x2, y2 = random.randint(0, tablero.tamaño -1), random.randint(0, tablero.tamaño - 1)
    direccion2 = random.choice ( ["horizontal", "vertical"] )
    barco2 = Barco(3, generar_coordenadas_barco(3, x2, y2, direccion2))

    tablero.agregar_barcos(barco1)
    tablero.agregar_barcos(barco2)

    tablero.mostrar_tablero()

    while not tablero.todos_barcos_hundidos():
        try:

            x = int(input("\nIngresa la coordenada X (0-8):"))
            y = int(input("Ingresa la coordenada Y (0-8):"))

            if 0 <= x < tablero.tamaño and 0 <= y < tablero.tamaño:
                tablero.recibir_disparo(x, y)
                tablero.mostrar_tablero()
            else:
                print("Las coordenadas no están en el rango")
        except ValueError:
            print("Introduce números enteros")