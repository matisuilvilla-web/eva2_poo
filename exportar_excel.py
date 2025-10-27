import openpyxl
from db.database import Database
from datetime import datetime

def exportar_empleados_a_excel():
    """Exporta los empleados a un archivo Excel."""
    # Creamos el libro de trabajo y la hoja activa
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Empleados"

    # Obtenemos los empleados desde la base de datos
    with Database().connect() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM empleados')
        empleados = cursor.fetchall()
    
    # Escribimos los encabezados (puedes cambiar los nombres según tu estructura de datos)
    ws.append(['ID', 'Nombre', 'Dirección', 'Teléfono', 'Email', 'Fecha de Contrato', 'Salario'])
    
    # Escribimos los datos de los empleados
    for empleado in empleados:
        # Si la fecha de contrato es un valor de tipo datetime, la convertimos a string
        fila = list(empleado)
        if isinstance(fila[5], datetime):  # Suponiendo que la fecha de contrato está en la columna 5
            fila[5] = fila[5].strftime("%Y-%m-%d")  # Formato de fecha: YYYY-MM-DD
        ws.append(fila)
    
    # Guardamos el archivo Excel
    archivo = "empleados.xlsx"
    wb.save(archivo)
    print(f"Empleados exportados a {archivo}")
