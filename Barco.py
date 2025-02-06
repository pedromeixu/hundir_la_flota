class Barco:
    def __init__ (self, tamaño, coordenadas):
        self.tamaño = tamaño
        self.coordenadas = coordenadas
        self.impactos = []

    def recibir_impacto (self, coordenada):
        if coordenada in self.coordenadas:
            self.impactos.append(coordenada)
            return True
        else:
            return False
            
    def hundido (self) -> bool:
        if len(self.impactos) == self.tamaño:
            return True
        else: 
            return False