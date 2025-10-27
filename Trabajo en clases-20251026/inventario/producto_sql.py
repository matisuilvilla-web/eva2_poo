import mysql.connector

#conexion a la base de datos
conexion = mysql.connector.connect(
    host="127.0.0.1",  #es mejor que localhost en windows
    user="root",
    # password="",
    database="ap_170"
)

if conexion.is_connected:
    print("Conectado")
else:
    print("No Conectado")

cursor = conexion.cursor() 
"""
cuando se hace  uso de mysql.connector.connect(...) se crea un objeto conexion a MySql
Desde esa conexion se puede comunicar con BD ,y ouedes:
- Enviar instrucciones sQL cursor.execute("<sentencia SQL>")
- Leer los resutados fila por fila del resultset (iterando el contenido del cursor)
- Mantengo un "puntero a la posición actual de lectura" 
"""

nombre = input("Ingrese nombre d eproducto: ")
precio = float(input("Precio de venta: "))
stock = int(input("Ingrese cantidad: "))

sql = """INSERT INTO producto (nombre, precio, stock) 
                    VALUES (%s, %s, %s)"""
cursor.execute(sql, (nombre,precio, stock))

conexion.commit()
print("Terminamos")


cursor.close()
conexion.close()