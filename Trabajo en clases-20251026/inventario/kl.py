import csv

archivo = r"C:\Users\lbm03\Desktop\datos.csv" #r de raw

with open(archivo, newline="", encoding="utf-8") as archivo:
    datos = csv.DictReader(archivo, delimiter=";")
    for fila in datos:
        print(fila["nombre"])