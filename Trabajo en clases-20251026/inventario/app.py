# app.py
from inventario import Inventario

def mostrar_menu():
    print("\n=== Control de Inventario (OOP) ===")
    print("1) Cargar inventario desde CSV")
    print("2) Listar productos")
    print("3) Agregar/Actualizar/Eliminar producto")
    print("4) Guardar inventario a CSV")
    print("0) Salir")

def submenu_crud(inv: Inventario):
    print("\n--- CRUD de productos ---")
    print("a) Agregar")
    print("b) Actualizar")
    print("c) Eliminar")
    print("x) Volver")

    opcion = input("Opción: ").strip().lower()
    try:
        if opcion == "a":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            stock  = int(input("Stock: "))
            p = inv.crear(codigo, nombre, precio, stock)
            print("Creado:", p.mostrar_info())

        elif opcion == "b":
            codigo = input("Código a actualizar: ")
            print("Deja vacío lo que no quieras cambiar.")
            n = input("Nuevo nombre: ").strip()
            pr = input("Nuevo precio: ").strip()
            st = input("Nuevo stock: ").strip()

            nuevo_nombre = n if n else None
            nuevo_precio = float(pr) if pr else None
            nuevo_stock  = int(st) if st else None

            p = inv.actualizar(codigo, nuevo_nombre, nuevo_precio, nuevo_stock)
            print("Actualizado:", p.mostrar_info())

        elif opcion == "c":
            codigo = input("Código a eliminar: ")
            inv.eliminar(codigo)
            print("Eliminado correctamente.")

        elif opcion == "x":
            return
        else:
            print("Opción inválida.")
    except Exception as e:
        print("Error:", e)

def main():
    inv = Inventario()
    salir = False

    while not salir:
        mostrar_menu()
        op = input("Opción: ").strip()

        if op == "1":
            inv.cargar_desde_csv()
            print("Inventario cargado (si existía data.csv).")
        elif op == "2":
            items = inv.listar()
            if not items:
                print("No hay productos.")
            else:
                for p in items:
                    print(p.mostrar_info())
        elif op == "3":
            submenu_crud(inv)
        elif op == "4":
            inv.guardar_a_csv()
            print("Inventario guardado en data.csv")
        elif op == "0":
            print("Adiós")
            salir = True
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
