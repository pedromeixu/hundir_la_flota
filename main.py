from Barco import Barco
from Tablero import Tablero
import random

if __name__ == "__main__":

    tablero = Tablero()

    barco1 = Barco(3, [random.randint(0, tablero.tamaño - 1), random.randint(0, tablero.tamaño - 1), (random.randint(0, tablero.tamaño - 1))] )
    barco2 = Barco(2, [random.randint(0, tablero.tamaño - 1), random.randint(0, tablero.tamaño - 1) ])

    tablero.agregar_barcos(barco1)
    tablero.agregar_barcos(barco2)

    tablero.mostrar_tablero()

    