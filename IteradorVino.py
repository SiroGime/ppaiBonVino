from IIterador import IIterador
class IteradorVino(IIterador):
    def __init__(self, coleccion):
        self.posicionActual = 0
        self.elementos = coleccion
        
    def primero(self):
        self.posicionActual = 0
        
    def haFinalizado(self):
        return self.posicionActual >= len(self.elementos)
    
    def actual(self):
        if not self.haFinalizado():
            return self.elementos[self.posicionActual]
        else:
            return None
        
    def cumpleFiltro(self, fecha_desde, fecha_hasta):
        if self.actual() is None:
            return False
        return self.actual().tenes_reseñas_de_tipo_en_periodo(fecha_desde, fecha_hasta)
    
    def siguiente(self):
        self.posicionActual += 1
        