# No cambia mucho: sigue mostrando menú, pero ahora usa la BD.
# app.py
from db_inventario import Inventario

def mostrar_menu():
    print("\n=== Control de Inventario (MySQL) ===")
    print("1) Listar productos")
    print("2) Agregar producto")
    print("3) Actualizar producto")
    print("4) Eliminar producto")
    print("0) Salir")

def main():
    inv = Inventario()
    salir = False

    while not salir:
        mostrar_menu()
        op = input("Opción: ").strip()

        try:
            if op == "1":
                items = inv.listar()
                if not items:
                    print("No hay productos.")
                else:
                    for p in items:
                        print(p.mostrar_info())
 
            elif op == "2":
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                stock = int(input("Stock: "))
                p = inv.crear(nombre, precio, stock)
                print("Creado:", p.mostrar_info())

            elif op == "3":
                id_txt = input("ID del producto a actualizar: ").strip()
                if not id_txt:
                    print("Debes indicar un ID.")
                    continue
                id_ = int(id_txt)
                nuevo_nombre = input("Nuevo nombre (vacío si no cambia): ").strip() or None

                pr = input("Nuevo precio (vacío si no cambia): ").strip()
                nuevo_precio = float(pr) if pr else None

                st = input("Nuevo stock (vacío si no cambia): ").strip()
                nuevo_stock = int(st) if st else None

                p = inv.actualizar(id_, nuevo_nombre, nuevo_precio, nuevo_stock)
                print("Actualizado:", p.mostrar_info())

            elif op == "4":
                id_txt = input("ID a eliminar: ").strip()
                if not id_txt:
                    print("Debes indicar un ID.")
                    continue
                id_ = int(id_txt)
                inv.eliminar(id_)
                print("Eliminado correctamente.")

            elif op == "0":
                print("Adiós")
                salir = True
            else:
                print("Opción inválida.")

        except Exception as e:
            print("Error:", e)

#pp
main()
