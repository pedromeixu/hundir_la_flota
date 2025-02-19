from Barco import Barco
class Tablero:
    def __init__(self, tamaño=8):
        self.tamaño = tamaño
        self.barcos = []
        self.disparos = []

    def agregar_barcos(self, barco):
        for barcos in self.barcos:
            for coordenadas in barcos:
                if coordenadas in barcos:
                    raise ValueError("Ya hay un barco en esa posición")
                else:
                    self.barcos.append(barco)
    
    def recibir_disparo(self, x, y):
        coordenadas = [x, y]
        if (x, y) in self.disparos:
            return "Ya disparaste ahí"
        else:
            self.disparos.append(coordenadas)

        for barco in self.barcos:
            if barco.recibir_impacto((x, y)):
                if barco.hundido() == True:
                    return "Hundido"
                else:
                    return "Tocado"
        
        return "Fallaste"
    
    def mostrar_tablero (self, ocultar_barcos=True):
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