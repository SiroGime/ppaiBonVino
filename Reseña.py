from datetime import datetime

class Reseña:
    def __init__(self,comentario,fecha_reseña,puntaje):
        self.comentario = comentario
        self.fecha_reseña = datetime.strptime(fecha_reseña,"%d/%m/%y")
        self.puntaje = puntaje

    def get_puntaje(self):
        return self.puntaje

    def sos_de_sommelier(self):
        if self.comentario == 'Sommelier':
            return True
        else:
            return False
        
    def sos_de_periodo(self, fecha_desde, fecha_hasta):
        if (fecha_desde <= self.fecha_reseña <= fecha_hasta):
            return True
        else:
            return False