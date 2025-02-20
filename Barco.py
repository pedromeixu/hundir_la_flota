class Barco:
    def __init__ (self, tamaño: int, coordenadas: list[tuple[int, int]]) -> None:
        self.tamaño = tamaño
        self.coordenadas = coordenadas
        self.impactos = []

    def recibir_impacto (self, coordenada: list[tuple[int, int]]) -> bool:
        """
        Registra un impacto en el barco si la coordenada coincide con una de sus posiciones
        """
        if coordenada in self.coordenadas:
            self.impactos.append(coordenada)
            return True
        else:
            return False
            
    def hundido (self) -> bool:
        """
        Verifica si el barco ha sido hundido, es decir, si todas sus posiciones han sido impactadas.
        """
        if len(self.impactos) == self.tamaño:
            return True
        else: 
            return False