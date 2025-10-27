import mysql.connector

#conexion a la base de datos
conexion = mysql.connector.connect(
    host="127.0.0.1",  #es mejor que localhost en windows
    user="root",
    # password="",
    database="ap_170"
)

cursor = conexion.cursor() 
nombre = input("Ingrese nombre de producto: ")
# cuando pregunte por el nombre escribe: x' or '1'='1
sql = f"SELECT * FROM producto WHERE nombre = '{nombre}'"
cursor.execute(sql)
filas = cursor.fetchall()
for f in filas:
    print(f)
print("Terminamos")
cursor.close()
conexion.close()