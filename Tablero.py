from Barco import Barco
import random
class Tablero:
    def __init__(self, tamaño: int = 5) -> None:
        self.tamaño = tamaño
        self.barcos = []
        self.disparos = []

    def coordenadas_validas(self, barco) -> bool:
        """
        Verifica si las coordenadas de un barco son válidas en el tablero
        """
        for coord in barco.coordenadas:
            if coord[0] < 0 or coord[0] >= self.tamaño or coord[1] < 0 or coord[1] >= self.tamaño:
                return False
            for b in self.barcos:
                if coord in b.coordenadas:
                    return False
        return True
    
    def agregar_barco_aleatorio(self, barco) -> None:
        """
        Coloca un barco en una posición aleatoria dentro del tablero.
        """
        direccion = random.choice ( ["horizontal", "vertical"] )
        while True:
            x = random.randint(0, self.tamaño - 1)
            y = random.randint(0, self.tamaño - 1)

            if direccion == "horizontal":
                if x + barco.tamaño <= self.tamaño:
                    coordenadas = [(x + i, y) for i in range(barco.tamaño)]
                else:
                    continue
            else:
                if y + barco.tamaño <= self.tamaño:
                    coordenadas = [(x, y + i) for i in range(barco.tamaño)]
                else:
                    continue
        
            barco.coordenadas = coordenadas

            if self.coordenadas_validas(barco):
                self.barcos.append(barco)
                break
    
    def recibir_disparo(self, x: int, y: int) -> str:
        """
        Registra un disparo en el tablero y evalúa si impactó un barco.
        """
        coordenadas = (x, y)
        if coordenadas in self.disparos:
            return "Ya disparaste ahí"
        else:
            self.disparos.append(coordenadas)

        for barco in self.barcos:
            if barco.recibir_impacto(coordenadas):
                if barco.hundido() == True:
                    return "Hundido"
                else:
                    return "Tocado"
        
        return "Fallaste"
    
    def mostrar_tablero (self) -> None:
        """
        Enseña el tablero
        """
        tablero = [["♥️" for i in range(self.tamaño)] for j in range(self.tamaño)]

        for y in range(self.tamaño):
            for x in range(self.tamaño):
                if (x, y) in self.disparos:
                    recibe_disparo = False
                    for barco in self.barcos:
                        if (x, y) in barco.coordenadas:
                            recibe_disparo = True
                            break
                    if recibe_disparo:
                        print("X", end=" ")
                    else:
                        print("*", end=" ")
                else:
                    print("♥️", end=" ")
            print()

    def todos_barcos_hundidos(self) -> bool:
        """
        Verifica si todos los barcos del tablero están hundidos
        """
        for barco in self.barcos:
            if not barco.hundido():
                return False
        return True