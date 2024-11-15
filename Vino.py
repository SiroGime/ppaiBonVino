from Bodega import Bodega
from Reseña import Reseña
from datetime import datetime
from IteradorReseña import IteradorReseña

class Vino:
    def __init__(self, annada, fecha_actualizacion, imagen_etiqueta, nombre, nota_de_cata_bodega, precio_ars, bodega, varietal, reseñas):
        self.annada = annada
        self.fecha_actualizacion = fecha_actualizacion
        self.imagen_etiqueta = imagen_etiqueta
        self.nombre = nombre
        self.nota_de_cata_bodega = nota_de_cata_bodega
        self.precio_ars = precio_ars
        self.bodega = bodega
        self.varietal = varietal
        self.reseñas = reseñas


    def conocer_etiqueta(self):
        return self.imagen_etiqueta

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio_ars

    def set_imagen_etiqueta(self):
        return self.imagen_etiqueta

    def set_nota_cata(self,nueva_cata):
        self.nota_de_cata_bodega = nueva_cata

    def set_precio(self,precioNuevo):
        self.precio_ars = precioNuevo
        
    def crearIterador(self, elementos):
        return IteradorReseña(elementos)       


    def tenes_reseñas_de_tipo_en_periodo(self, fechaDesde, fechaHasta):
        fechaDesde = datetime.strptime(fechaDesde,"%m/%d/%y")
        fechaHasta = datetime.strptime(fechaHasta,"%m/%d/%y")
        reseñas_en_periodo = []
        
        iteradorReseña = self.crearIterador(self.reseñas)
        iteradorReseña.primero()
        while not iteradorReseña.haFinalizado():
            if iteradorReseña.cumpleFiltro(fechaDesde, fechaHasta):
                reseña = iteradorReseña.actual()
                reseñas_en_periodo.append(reseña)
            iteradorReseña.siguiente()
                
        return reseñas_en_periodo
    
    def calcularPuntajePromedioDeSommelierEnPeriodo(self, reseñas):
        cantidad_reseñas = 0
        total_puntajes = 0
        iteradorReseña = self.crearIterador(reseñas)
        iteradorReseña.primero()
        while not iteradorReseña.haFinalizado():
            if iteradorReseña.cumpleFiltro(soloSommelier=True):
                reseña = iteradorReseña.actual()
                cantidad_reseñas += 1 
                total_puntajes += reseña.get_puntaje()
            iteradorReseña.siguiente()
        
        return cantidad_reseñas, total_puntajes
            
            
