from IIterador import IIterador
class IteradorReseña(IIterador):
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
        
    def cumpleFiltro(self, fecha_desde=None, fecha_hasta=None, soloSommelier=False):
        if self.actual() is None:
            return False
        
        if soloSommelier:
            return self.actual().sos_de_sommelier()
        
        return self.actual().sos_de_periodo(fecha_desde, fecha_hasta) and self.actual().sos_de_sommelier()
    
    def siguiente(self):
        self.posicionActual += 1