import Vino
from InterfazExcel import InterfazExcel
from InterfazPdf import InterfazPdf
from crearVinos import crear_vinos
from datetime import datetime
from IAgregado import IAgregado
from IteradorVino import IteradorVino

class GestorRankingVinos(IAgregado):
    def __init__(self):
        self.fecha_desde = None
        self.fecha_hasta = None
        self.tipo_ranking_seleccionada = None
        self.vinos_ordenados = []
        self.vinos_que_cumplen_filtros = []
        self.interfaz = InterfazExcel()


    def opcion_generar_ranking_vinos(self, estado):
        if estado:
            print("Solicitar fechas")
            return True
        
    def tomarSelFechaDesdeHasta(self,fechaDesde, fechaHasta):
        self.fecha_desde = fechaDesde
        self.fecha_hasta = fechaHasta
        return True
    
    def tomarSelTipoReseña(self,tipo_reseña):
        tipo_reseña = str(tipo_reseña)
        return True
    
    def tomarSelTipoVisualizacion(self):
        return True
    
    def confirmarExportacion(self, tipo_visualizacion):
        if tipo_visualizacion == "Excel":
            self.interfaz = InterfazExcel()
            self.interfaz.exportar_excel(self.vinos_ordenados)
        elif tipo_visualizacion == "Pdf":
            self.interfaz = InterfazPdf()
            self.interfaz.exportar_pdf(self.vinos_ordenados)
        return True
    
    def tomarConfirmacionGenRepo(self):
        return True

    def buscarVinosConReservasEnPeriodo(self):
        vinos = crear_vinos()
        iteradorVino = self.crearIterador(vinos)
        iteradorVino.primero()
        while not iteradorVino.haFinalizado():
            vino = iteradorVino.actual() 
            reseña = iteradorVino.cumpleFiltro(self.fecha_desde, self.fecha_hasta)
            
            nombreVino = vino.nombre
            bodega = vino.bodega.nombre
            precio = vino.precio_ars
            region, pais = vino.bodega.obtener_region_y_pais()
            varietal_descripcion = vino.varietal.descripcion
            if reseña:
                self.vinos_que_cumplen_filtros.append({
                    "vino_objeto": vino,
                    "nombre_vino": nombreVino,
                    "precio_sugerido":precio,
                    "bodega": bodega,
                    "region": region,
                    "pais": pais,
                    "varietal_descripcion": varietal_descripcion,
                    'Reseñas': reseña,
                    'Promedio de la Calificacion de reseña':None
                })
                
            iteradorVino.siguiente()
                
    def crearIterador(self, elementos):
        return IteradorVino(elementos)       

    def mostrarDatos(self):
        contador = 0
        for vino in self.vinos_ordenados:
            if contador == 10:
                break
            print('---')
            print(f"Nombre del vino: {vino['nombre_vino']}")
            print(f"Precio Sugerido: ${vino['precio_sugerido']}")
            print(f"Bodega: {vino['bodega']}")
            print(f"Región: {vino['region']}")
            print(f"País: {vino['pais']}")
            print(f"Varietal: {vino['varietal_descripcion']}")
            print("Reseñas:")
            for reseña in vino['Reseñas']:
                print(f"  - Comentario: {reseña.comentario}, Fecha: {reseña.fecha_reseña}, Calificacion de somelier: {reseña.get_puntaje()}")
            print(f"Calificacion General: {vino['Promedio de la Calificacion de reseña']}")
            contador +=1
        
    def buscarPuntajeDeSommelierEnPeriodo(self):
        for vino_dict in self.vinos_que_cumplen_filtros:
            vino = vino_dict['vino_objeto']
            cantidad_reseñas, total_puntajes = vino.calcularPuntajePromedioDeSommelierEnPeriodo(vino_dict["Reseñas"])
            promedio_puntajes = self.calcularPuntajePromedio(cantidad_reseñas, total_puntajes)
            vino_dict['Promedio de la Calificacion de reseña'] = promedio_puntajes
    
    def calcularPuntajePromedio(self, cantidad_reseñas, total_puntajes):
        if cantidad_reseñas > 0:
                promedio_puntajes = total_puntajes / cantidad_reseñas
        else:
            promedio_puntajes = 0
        
        return promedio_puntajes

    def ordenarVinos(self):
        n = len(self.vinos_que_cumplen_filtros)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.vinos_que_cumplen_filtros[j]['Promedio de la Calificacion de reseña'] < self.vinos_que_cumplen_filtros[j + 1]['Promedio de la Calificacion de reseña']:
                    # Intercambiar si el promedio del vino actual es menor que el siguiente
                    temp = self.vinos_que_cumplen_filtros[j]
                    self.vinos_que_cumplen_filtros[j] = self.vinos_que_cumplen_filtros[j + 1]
                    self.vinos_que_cumplen_filtros[j + 1] = temp
        
        # Guardar los vinos ordenados en self.vinos_ordenados
        self.vinos_ordenados = self.vinos_que_cumplen_filtros
        
        # Guardar los vinos ordenados en self.vinos_ordenados
        self.vinos_ordenados = self.vinos_que_cumplen_filtros

        print("Vinos ordenados por promedio de puntaje de reseña:")

    def finCu(self,vari):
        if vari:
            return True