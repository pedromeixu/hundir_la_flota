from Barco import Barco
class Tablero:
    def __init__(self, tamaño=5):
        self.tamaño = tamaño
        self.barcos = []
        self.disparos = []

    def agregar_barcos(self, barco):
        for b in self.barcos:
            for coord_b in b.coordenadas:
                for coord_nueva in barco.coordenadas:
                    if coord_b == coord_nueva:
                        raise ValueError("Ya hay un barco en esa posición")
        self.barcos.append(barco)

    
    def recibir_disparo(self, x, y):
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

    def todos_barcos_hundidos(self):
        for barco in self.barcos:
            if not barco.hundido():
                return False
        return True