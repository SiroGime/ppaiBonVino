from Pais import Pais
from Provincia import Provincia
from RegionVitivinicola import RegionVitivinicola
from Bodega import Bodega
from Varietal import Varietal
from Reseña import Reseña
from Vino import Vino
from datetime import datetime, timedelta
import random


def crear_vinos():
    # Nombres inventados para países, provincias y regiones
    paises = [Pais("Argentina"), Pais("Chile"), Pais("España")]

    # Nombres inventados para bodegas
    nombres_bodegas = ["Bodega Aurora", "Viña del Sol", "Casa de Vinos", "La Bodega Encantada", "El Viñedo Alegre"]

    # Crear lista de provincias
    provincias = [Provincia("Mendoza", paises[0]), Provincia("San Juan", paises[0]), Provincia("Valparaíso", paises[1])]

    # Crear lista de regiones vitivinícolas
    regiones = [RegionVitivinicola("Valle de Uco", "Valle de Uco", provincias[0].obtener_pais()), 
                RegionVitivinicola("Maipo Valley", "Maipo Valley", provincias[2].obtener_pais())]

    # Crear lista de bodegas con historias inventadas y fechas aleatorias en el 2024
    bodegas = [Bodega(nombres_bodegas[i], datetime(2024, random.randint(1, 12), random.randint(1, 28)).strftime('%d/%m/%y'), 
                      f"Historia de la {nombres_bodegas[i]}", nombres_bodegas[i], random.randint(300, 800), regiones[i % 2]) for i in range(len(nombres_bodegas))]

    # Crear lista de varietales
    varietales = [Varietal("Malbec", 100), Varietal("Cabernet Sauvignon", 100)]

    # Crear lista de reseñas con distintas fechas en el año 2024
    # Definir el rango de fechas
    fecha_inicial = datetime(2024, 1, 1)
    fecha_final = datetime(2024, 12, 31)

    # Calcular la cantidad de días entre las fechas inicial y final
    diferencia_dias = (fecha_final - fecha_inicial).days

    # Generar las reseñas con fechas aleatorias en el rango definido
    reseñas = [Reseña(random.choice(["Sommelier", "Amigo", "Normal"]), (fecha_inicial + timedelta(days=random.randint(0, diferencia_dias))).strftime('%d/%m/%y'), random.randint(50, 100)) for _ in range(80)]

    # Crear lista de vinos con nombres inventados
    vinos = []
    for i in range(20):
        nombre = f"Vino {i+1}"  # Nombre inventado para el vino
        annada = random.randint(2000, 2023)
        fecha_actualizacion = "2024-01-01"
        imagen_etiqueta = f"etiqueta_{i+1}.jpg"  # Nombre de imagen inventado
        nota_de_cata_bodega = f"Nota de cata de {nombre}"  # Nota de cata con referencia al nombre del vino
        precio_ars = random.randint(500, 5000)
        bodega = random.choice(bodegas)  # Se elige una bodega aleatoria de la lista de bodegas
        varietal = random.choice(varietales)  # Se elige un varietal aleatorio de la lista de varietales
        
        # Asignar 2 reseñas por vino
        vino_reseñas = random.sample(reseñas, 10)
        
        vino = Vino(annada, fecha_actualizacion, imagen_etiqueta, nombre, nota_de_cata_bodega, precio_ars, bodega, varietal, vino_reseñas)
        vinos.append(vino)

    # Imprimir información de los vinos para verificar
    for vino in vinos:
        print(f"Nombre: {vino.get_nombre()}, Precio: {vino.get_precio()}, Bodega: {vino.bodega.get_nombre()}, Varietal: {vino.varietal.get_descripcion()}")
        for reseña in vino.reseñas:
            print(f"  Reseña: {reseña.comentario}, Fecha: {reseña.fecha_reseña}, Puntaje: {reseña.get_puntaje()}")
    
    return vinos
