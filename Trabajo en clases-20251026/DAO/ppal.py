from persona import Persona
from persona_dao import PersonaDAO

# Crear instancia de PersonaDAO
persona_dao = PersonaDAO()

# Crear nueva persona
nueva_persona = Persona(None, 'Juan Perez', 30)
persona_dao.insertar(nueva_persona)
print(f'Persona insertada: {nueva_persona}')

# Seleccionar todas las personas
personas = persona_dao.seleccionar_todos()
print('Lista de personas:')
for persona in personas:
    print(persona)

# Actualizar una persona
if personas:
    persona_actualizar = personas[0]
    persona_actualizar.nombre = 'Juan Actualizado'
    persona_actualizar.edad = 35
    persona_dao.actualizar(persona_actualizar)
    print(f'Persona actualizada: {persona_actualizar}')

# Eliminar una persona
if personas:
    persona_eliminar = personas[0]
    persona_dao.eliminar(persona_eliminar.id_persona)
    print(f'Persona eliminada: {persona_eliminar.id_persona}')
