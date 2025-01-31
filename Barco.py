class Barco:
    tamaño: int
    posicion: list
    impactos: int

    def __init__ (self, tamaño, posicion):
        self.tamaño = tamaño
        self.posicion = posicion
        self.impactos = 0
    
    def hundido (self) -> bool:
        if self.impactos == self.tamaño:
            return True
        else: 
            return False