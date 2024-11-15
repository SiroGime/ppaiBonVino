
class Bodega:
    def __init__(self,descripcion,fecha_ultima_actualizacion,historia,nombre,periodo_actualizacion,region):
        self.descripcion = descripcion
        self.fecha_ultima_actualizacion = fecha_ultima_actualizacion
        self.historia = historia
        self.nombre = nombre
        self.periodo_actualizacion = periodo_actualizacion
        self.RegionVitivinicola = region

    def get_nombre(self):
        return self.nombre

    def obtener_region_y_pais(self):
        return self.RegionVitivinicola.get_nombre(), self.RegionVitivinicola.obtener_pais()