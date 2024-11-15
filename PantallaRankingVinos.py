import tkinter as tk
import os
from tkinter import PhotoImage, messagebox
from tkcalendar import Calendar  # Librería externa para el calendario
from GestorRankingVinos import GestorRankingVinos
from datetime import datetime
from tkinter import ttk
class PantallaRankingVinos:
    def __init__(self):
        self.fechaDesdelbl = None
        self.fechaHastalbl = None
        self.fechaDesdetxt = None
        self.fechaHastatxt = None
        self.root = tk.Tk()
        self.root.title("Ranking de Vinos")
        self.root.geometry("679x544")  # Establece las dimensiones de la ventana
        self.root.resizable(False, False)  # Hace que la ventana no sea redimensionable

        # Carga la imagen de fondo
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Obtiene el directorio del script actual
        image_path = os.path.join(script_dir, "pantalla.png")  # Construye la ruta completa de la imagen
        
        self.background_image = PhotoImage(file=image_path)

        # Coloca la imagen de fondo en un label
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Creamos el botón "Generar ranking vinos"
        self.btn_generar_ranking = tk.Button(self.root, text="Generar ranking vinos", command=self.opcion_generar_ranking_vinos)
        self.btn_generar_ranking.place(relx=0.5, rely=0.5, anchor="center", y=27)

        self.gestor = GestorRankingVinos()

    def opcion_generar_ranking_vinos(self):
        respuesta = self.gestor.opcion_generar_ranking_vinos(True)
        if respuesta:
            self.btn_generar_ranking.destroy()  # Eliminamos el botón "Generar ranking vinos"
            self.mostrar_ingresar_fechas()

    def mostrar_ingresar_fechas(self):
        # Crear los atributos para las fechas
        self.fecha_desde_lbl = tk.Label(self.root, text="Fecha desde:")
        self.fecha_desde_lbl.place(relx=0.3, rely=0.25, anchor="center")  # 1 cm más abajo

        self.calendario_desde = Calendar(self.root, selectmode="day", year=2024, month=1, day=1)
        self.calendario_desde.place(relx=0.3, rely=0.50, anchor="center")  # 1 cm más abajo

        self.fecha_hasta_lbl = tk.Label(self.root, text="Fecha hasta:")
        self.fecha_hasta_lbl.place(relx=0.7, rely=0.25, anchor="center")  # 1 cm más abajo

        self.calendario_hasta = Calendar(self.root, selectmode="day", year=2024, month=1, day=1)
        self.calendario_hasta.place(relx=0.7, rely=0.50, anchor="center")  # 1 cm más abajo

        # Botón para guardar las fechas
        self.btn_guardar_fechas = tk.Button(self.root, text="Guardar", command=self.validar_periodo)
        self.btn_guardar_fechas.place(relx=0.5, rely=0.75, anchor="center")

    def validar_periodo(self):
        fecha_desde = self.calendario_desde.get_date()
        fecha_hasta = self.calendario_hasta.get_date()
        
        # Convertir las fechas en objetos datetime
        fecha_desde_dt = datetime.strptime(fecha_desde, "%m/%d/%y").strftime("%d/%m/%y")
        fecha_hasta_dt = datetime.strptime(fecha_hasta, "%m/%d/%y").strftime("%d/%m/%y")
        
        # Validar las fechas
        if fecha_desde_dt < fecha_hasta_dt:
            print("Fechas válidas. Desde:", fecha_desde, "Hasta:", fecha_hasta)
            self.fechaDesdetxt = fecha_desde
            self.fechaHastatxt = fecha_hasta
            respuesta = self.gestor.tomarSelFechaDesdeHasta(fecha_desde, fecha_hasta)
            if respuesta:
                print('gestor tiene las fechas')
                self.fecha_desde_lbl.destroy()
                self.calendario_desde.destroy()
                self.fecha_hasta_lbl.destroy()
                self.calendario_hasta.destroy()
                self.btn_guardar_fechas.destroy()
                self.tomar_tipo_reseña()
        else:
            messagebox.showerror("Error", "Por favor, ingrese fechas válidas (Fecha desde debe ser menor o igual que Fecha hasta)")
            
            

    def tomar_tipo_reseña(self):
        # Crear el título y el combobox para seleccionar el tipo de reseña
        self.tipo_reseña_lbl = tk.Label(self.root, text="Elegir tipo de Reseña:")
        self.tipo_reseña_lbl.place(relx=0.5, rely=0.55, anchor="center")

        self.tipo_reseña_cb = ttk.Combobox(self.root, values=["Normales", "amigos", "Somelier"], state="readonly")
        self.tipo_reseña_cb.place(relx=0.5, rely=0.65, anchor="center")
        self.tipo_reseña_cb.current(0)  # Establecer el valor por defecto

        # Botón para confirmar la selección de tipo de reseña
        self.btn_confirmar_tipo_reseña = tk.Button(self.root, text="Seleccionar", command=self.confirmar_tipo_reseña)
        self.btn_confirmar_tipo_reseña.place(relx=0.5, rely=0.75, anchor="center")

    def confirmar_tipo_reseña(self):
        tipo_reseña = self.tipo_reseña_cb.get()
        if tipo_reseña == "Somelier":
            print(f"Tipo de reseña seleccionado: {tipo_reseña}")
            # acciones con el tipo de reseña seleccionado
            #Patron
            respuesta = self.gestor.tomarSelTipoReseña(tipo_reseña)
            if respuesta:
                print('Tipo de reseña enviado al gestor')
                # Realizar las acciones necesarias después de enviar el tipo de reseña al gestor
                self.tipo_reseña_lbl.destroy()
                self.tipo_reseña_cb.destroy()
                self.btn_confirmar_tipo_reseña.destroy()
                self.tomarTipoVisualizacion()
        else:
            messagebox.showerror("Error", "Por favor, seleccione el tipo de reseña Sommelier.")
    

    def tomarTipoVisualizacion(self):
        self.tipo_visualizacion_lbl = tk.Label(self.root, text="Elegir tipo de Visualizacion:")
        self.tipo_visualizacion_lbl.place(relx=0.5, rely=0.55, anchor="center")

        self.tipo_visualizacion_cb = ttk.Combobox(self.root, values=["Pdf", "Excel", "Pantalla"], state="readonly")
        self.tipo_visualizacion_cb.place(relx=0.5, rely=0.65, anchor="center")
        self.tipo_visualizacion_cb.current(0)

        # Botón para confirmar la selección de tipo de visualizacion
        self.btn_confirmar_tipo_visualizacion = tk.Button(self.root, text="Seleccionar", command=self.confirmar_tipo_visualizacion)
        self.btn_confirmar_tipo_visualizacion.place(relx=0.5, rely=0.75, anchor="center")    
    
    def confirmar_tipo_visualizacion(self):
        tipo_visualizacion = self.tipo_visualizacion_cb.get()
        if tipo_visualizacion:
            print(f"Tipo de visualizacion seleccionado: {tipo_visualizacion}")
            #Patron 
            respuesta = self.gestor.tomarSelTipoVisualizacion()
            if respuesta:
                print('Tipo de visualizacion enviado al gestor')
                self.tipo_visualizacion_lbl.destroy()
                self.tipo_visualizacion_cb.destroy()
                self.btn_confirmar_tipo_visualizacion.destroy()
                self.tomarConfirmacionGenRepo(tipo_visualizacion)
        else:
            messagebox.showerror("Error", "Por favor, seleccione un tipo de visualizacion.")
    
    def tomarConfirmacionGenRepo(self,tipo_visualizacion):
        self.lbl_pregunta = tk.Label(self.root, text="¿Desea confirmar el registro del reporte?")
        self.lbl_pregunta.place(relx=0.5, rely=0.55, anchor="center")
        self.lbl_preguntapositiva = tk.Button(self.root, text="Generar informe", command=lambda:self.confirmacion_generacion_informe("Si",tipo_visualizacion))
        self.lbl_preguntapositiva.place(relx=0.35, rely=0.65, anchor="center", y=27)
        self.lbl_preguntanegativa = tk.Button(self.root, text="No generar informe", command=lambda:self.confirmacion_generacion_informe("No",tipo_visualizacion))
        self.lbl_preguntanegativa.place(relx=0.65, rely=0.65, anchor="center", y=27)


    def confirmacion_generacion_informe(self,eleccion,tipo_visualizacion):
        print(eleccion)
        if eleccion == "Si":
            #Patron
            confirmacion = self.gestor.tomarConfirmacionGenRepo()
            if confirmacion and tipo_visualizacion == "Excel":
                self.lbl_pregunta.destroy()
                self.lbl_preguntapositiva.destroy()
                self.lbl_preguntanegativa.destroy()
                self.gestor.buscarVinosConReservasEnPeriodo()
                self.gestor.buscarPuntajeDeSommelierEnPeriodo()
                self.gestor.ordenarVinos()
                self.gestor.mostrarDatos()
                self.pedirConfirmacionExportacion(tipo_visualizacion)
            elif confirmacion and tipo_visualizacion == "Pdf":
                self.lbl_pregunta.destroy()
                self.lbl_preguntapositiva.destroy()
                self.lbl_preguntanegativa.destroy()
                self.gestor.buscarVinosConReservasEnPeriodo()
                self.gestor.buscarPuntajeDeSommelierEnPeriodo()
                self.gestor.ordenarVinos()
                self.gestor.mostrarDatos()
                self.pedirConfirmacionExportacion(tipo_visualizacion)
            else:
                self.lbl_pregunta.destroy()
                self.lbl_preguntapositiva.destroy()
                self.lbl_preguntanegativa.destroy()
                self.fin_cus = tk.Label(self.root, text="Se Mostrara el informe en pantalla")
                self.fin_cus.place(relx=0.5, rely=0.55, anchor="center")
                fin_cu=self.gestor.finCu(True)
                if fin_cu:
                    # Termina el caso de uso
                    self.fin_cus = tk.Label(self.root, text="Fin de caso de uso")
                    self.fin_cus.place(relx=0.5, rely=0.6, anchor="center")
        else:
            print("Se ha cancelado el registro del reporte.")
            print("Fin caso de uso.")
            fin_cu=self.gestor.finCu(True)
            if fin_cu:
                # Termina el caso de uso
                self.lbl_pregunta.destroy()
                self.lbl_preguntapositiva.destroy()
                self.lbl_preguntanegativa.destroy()
                self.fin_cus = tk.Label(self.root, text="Fin de caso de uso")
                self.fin_cus.place(relx=0.5, rely=0.55, anchor="center")


    def pedirConfirmacionExportacion(self,tipo_visualizacion):
        self.lbl_pregunta_exportacion = tk.Label(self.root, text="¿Confirmar la exportacion?")
        self.lbl_pregunta_exportacion.place(relx=0.5, rely=0.55, anchor="center")
        self.lbl_preguntapositiva_export = tk.Button(self.root, text="Generar exportacion", command=lambda:self.tomarConfirmacionExportacion("Si",tipo_visualizacion))
        self.lbl_preguntapositiva_export.place(relx=0.35, rely=0.65, anchor="center", y=27)
        self.lbl_preguntanegativa_export = tk.Button(self.root, text="No generar exportacion", command=lambda:self.tomarConfirmacionExportacion("No",tipo_visualizacion))
        self.lbl_preguntanegativa_export.place(relx=0.65, rely=0.65, anchor="center", y=27)


    def tomarConfirmacionExportacion(self,respuesta,tipo_visualizacion):
        if respuesta == "Si":
            if  tipo_visualizacion == "Excel":
                self.gestor.confirmarExportacion(tipo_visualizacion)
                self.lbl_pregunta_exportacion.destroy()
                self.lbl_preguntapositiva_export.destroy()
                self.lbl_preguntanegativa_export.destroy()
                self.fin_cus = tk.Label(self.root, text="El Excel se genero con exito")
                self.fin_cus.place(relx=0.5, rely=0.55, anchor="center")
                self.fin_cus = tk.Label(self.root, text="Fin de caso de uso")
                self.fin_cus.place(relx=0.5, rely=0.60, anchor="center")
            elif tipo_visualizacion == "Pdf":
                self.gestor.confirmarExportacion(tipo_visualizacion)
                self.lbl_pregunta_exportacion.destroy()
                self.lbl_preguntapositiva_export.destroy()
                self.lbl_preguntanegativa_export.destroy()
                self.fin_cus = tk.Label(self.root, text="El Pdf se genero con exito")
                self.fin_cus.place(relx=0.5, rely=0.55, anchor="center")
                self.fin_cus = tk.Label(self.root, text="Fin de caso de uso")
                self.fin_cus.place(relx=0.5, rely=0.60, anchor="center")
        else:
            fin_cu=self.gestor.finCu(True)
            if fin_cu:
                # Termina el caso de uso
                self.lbl_pregunta_exportacion.destroy()
                self.lbl_preguntapositiva_export.destroy()
                self.lbl_preguntanegativa_export.destroy()
                self.fin_cus = tk.Label(self.root, text="Fin de caso de uso")
                self.fin_cus.place(relx=0.5, rely=0.55, anchor="center")

    
    def iniciar(self):
        self.root.mainloop()

# Creamos una instancia de la clase PantallaRankingVinos
pantalla = PantallaRankingVinos()
# Iniciamos la aplicación
pantalla.iniciar()
