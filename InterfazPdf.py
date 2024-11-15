from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

class InterfazPdf:
    def exportar_pdf(self, vinos):
        # Crear el documento PDF
        pdf_filename = "ranking_vinos.pdf"
        document = SimpleDocTemplate(pdf_filename, pagesize=letter)

        # Crear los datos para la tabla
        data = [
            ['Nombre del Vino', 'Bodega', 'Región', 'País', 'Varietal', 'Promedio de Puntaje de Reseña', 'Precio Sugerido']  # Encabezados
        ]

        # Agregar los datos de los vinos
        for vino in vinos:
            row = [
                vino['nombre_vino'],
                vino['bodega'],
                vino['region'],
                vino['pais'],
                vino['varietal_descripcion'],
                vino.get('Promedio de la Calificacion de reseña', "N/A"),
                vino.get('precio_sugerido', "N/A")
            ]
            data.append(row)

        # Crear la tabla
        table = Table(data)

        # Establecer el estilo de la tabla
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        # Construir el documento PDF con la tabla
        document.build([table])

        print(f"Archivo PDF '{pdf_filename}' creado exitosamente.")

        return True