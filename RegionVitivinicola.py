from Pais import Pais
class RegionVitivinicola:
    def __init__(self,descripcion,nombre,pais):
        self.descripcion = descripcion
        self.nombre = nombre
        self.pais = pais

    def get_nombre(self):
        return self.nombre

    def obtener_pais(self):
        return self.pais.get_nombre()