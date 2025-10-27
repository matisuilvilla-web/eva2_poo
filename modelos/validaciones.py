import re

def validar_email(email):
    """Valida que el email tenga el formato correcto"""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def validar_telefono(telefono):
    """Valida que el teléfono tenga el formato correcto (10 dígitos)"""
    pattern = r'^\d{10}$'
    return re.match(pattern, telefono)
