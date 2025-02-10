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