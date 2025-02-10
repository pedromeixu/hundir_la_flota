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