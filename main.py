from DAO.empleadoDAO import EmpleadoDAO
from DAO.departamentoDAO import DepartamentoDAO
from DAO.proyectoDAO import ProyectoDAO
from DAO.registro_tiempoDAO import RegistroTiempoDAO
from DAO.usuarioDAO import UsuarioDAO
from modelos.empleado import Empleado
from modelos.departamento import Departamento
from modelos.proyecto import Proyecto
from modelos.registro_tiempo import RegistroTiempo
from modelos.usuario import Usuario
from exportar_excel import exportar_empleados_a_excel
from modelos.validaciones import validar_email, validar_telefono    



# Crear instancias de los DAOs
empleado_dao = EmpleadoDAO('eva2.db')  # Ruta de la base de datos
departamento_dao = DepartamentoDAO('eva2.db')
proyecto_dao = ProyectoDAO('eva2.db')
registro_tiempo_dao = RegistroTiempoDAO('eva2.db')
usuario_dao = UsuarioDAO('eva2.db')

# Funciones de interacción con el menú

def iniciar_sesion():
    """Función para iniciar sesión."""
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    usuario_dao = UsuarioDAO()
    usuario = usuario_dao.autenticar(username)
     
    if usuario and usuario.check_password(password):  # Verificamos si la contraseña coincide
        print(f"Bienvenido {usuario.nombre}!")
        if usuario.rol == 'admin':
            print("Acceso de Administrador concedido.")
        else:
            print("Acceso de usuario concedido.")
    else:
        print("Credenciales incorrectas.")

def mostrar_menu():
    """Muestra el menú principal"""
    print("\nMenú del Sistema")
    print("1. Registrar Empleado")
    print("2. Editar Empleado")
    print("3. Eliminar Empleado")
    print("4. Listar Empleados")
    print("5. Crear Departamento")
    print("6. Editar Departamento")
    print("7. Eliminar Departamento")
    print("8. Asignar Proyecto a Empleado")
    print("9. Registrar Horas Trabajadas")
    print("10. Registrar Usuario")
    print("11. Exportar Empleados a Excel")
    print("0. Salir")

def pedir_datos_empleado():
    """Solicita los datos para crear o editar un empleado"""
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    fecha_contrato = input("Fecha de contrato (YYYY-MM-DD): ")
    salario = float(input("Salario: "))
    return nombre, direccion, telefono, email, fecha_contrato, salario

def pedir_datos_departamento():
    """Solicita los datos para crear o editar un departamento"""
    nombre_depto = input("Nombre del departamento: ")
    gerente_id = int(input("ID del gerente (empleado): "))
    return nombre_depto, gerente_id

def pedir_datos_usuario():
    """Solicita los datos para crear un nuevo usuario"""
    nombre = input("Nombre: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    contraseña = input("Contraseña: ")
    rol = input("Rol (empleado, administrador): ")
    return nombre, email, telefono, contraseña, rol

def registrar_empleado():
    """Registra un nuevo empleado"""
    nombre, direccion, telefono, email, fecha_contrato, salario = pedir_datos_empleado()
    nuevo_empleado = Empleado(None, nombre, direccion, telefono, email, fecha_contrato, salario)
    empleado_dao.insertar(nuevo_empleado)
    print("Empleado registrado con éxito")

def editar_empleado():
    """Edita los datos de un empleado"""
    id_empleado = int(input("ID del empleado a editar: "))
    nombre, direccion, telefono, email, fecha_contrato, salario = pedir_datos_empleado()
    empleado = Empleado(id_empleado, nombre, direccion, telefono, email, fecha_contrato, salario)
    empleado_dao.actualizar(empleado)
    print("Empleado actualizado con éxito")

def eliminar_empleado():
    """Elimina un empleado"""
    id_empleado = int(input("ID del empleado a eliminar: "))
    empleado_dao.eliminar(id_empleado)
    print("Empleado eliminado con éxito")

def listar_empleados():
    """Lista todos los empleados"""
    empleados = empleado_dao.seleccionar_todos()
    if not empleados:
        print("No hay empleados registrados.")
    else:
        for emp in empleados:
            print(f"ID: {emp.id_empleado}, Nombre: {emp.nombre}, Teléfono: {emp.telefono}, Email: {emp.email}, Fecha de Contrato: {emp.fecha_contrato}, Salario: {emp.salario}")

def crear_departamento():
    """Crea un nuevo departamento"""
    nombre_depto, gerente_id = pedir_datos_departamento()
    depto = Departamento(None, nombre_depto, gerente_id)
    departamento_dao.insertar(depto)
    print("Departamento creado con éxito")

def editar_departamento():
    """Edita un departamento existente"""
    id_departamento = int(input("ID del departamento a editar: "))
    nuevo_nombre, nuevo_gerente_id = pedir_datos_departamento()
    depto = Departamento(id_departamento, nuevo_nombre, nuevo_gerente_id)
    departamento_dao.actualizar(depto)
    print("Departamento actualizado con éxito")

def eliminar_departamento():
    """Elimina un departamento"""
    id_departamento = int(input("ID del departamento a eliminar: "))
    departamento_dao.eliminar(id_departamento)
    print("Departamento eliminado con éxito")

def asignar_proyecto_empleado():
    """Asigna un proyecto a un empleado"""
    id_empleado = int(input("ID del empleado: "))
    id_proyecto = int(input("ID del proyecto: "))
    
    # Obtener el proyecto por ID
    proyecto = proyecto_dao.seleccionar_por_id(id_proyecto)
    
    if proyecto:
        # Aquí asumo que la clase Proyecto tiene un método asignar_empleado
        proyecto.asignar_empleado(id_empleado)  # Esta línea depende de cómo hayas implementado la asignación en la clase Proyecto
        print(f"Empleado {id_empleado} asignado al proyecto {id_proyecto}")
    else:
        print(f"No se encontró un proyecto con ID {id_proyecto}")

def registrar_horas_trabajadas():
    """Registra las horas trabajadas por un empleado"""
    id_empleado = int(input("ID del empleado: "))
    id_proyecto = int(input("ID del proyecto: "))
    horas = float(input("Horas trabajadas: "))
    descripcion = input("Descripción del trabajo: ")
    registro = RegistroTiempo(None, id_empleado, id_proyecto, horas, descripcion)
    registro_tiempo_dao.insertar(registro)
    print("Horas registradas con éxito")

def registrar_usuario():
    """Registra un nuevo usuario"""
    nombre, email, telefono, contraseña, rol = pedir_datos_usuario()
    usuario = Usuario(None, nombre, email, telefono, contraseña, rol)
    usuario.password = usuario.hash_password()
    usuario_dao.insertar(usuario)
    print(f"Usuario {nombre} registrado con éxito")

def menu_empleado():
    """Muestra el menú de opciones para empleados"""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_empleado()
        elif opcion == '2':
            editar_empleado()
        elif opcion == '3':
            eliminar_empleado()
        elif opcion == '4':
            listar_empleados()
        elif opcion == '5':
            crear_departamento()
        elif opcion == '6':
            editar_departamento()
        elif opcion == '7':
            eliminar_departamento()
        elif opcion == '8':
            asignar_proyecto_empleado()
        elif opcion == '9':
            registrar_horas_trabajadas()
        elif opcion == '10':
            registrar_usuario()
        elif opcion == '11':
            exportar_empleados_a_excel()
        elif opcion == '0':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

def main():
    """Función principal que inicia el sistema"""
    menu_empleado()

if __name__ == "__main__":
    main()

def menu_informe():
    print("1. Exportar empleados a Excel")
    opcion = input("Seleccione una opción: ")

    if opcion == "11":
        exportar_empleados_a_excel()