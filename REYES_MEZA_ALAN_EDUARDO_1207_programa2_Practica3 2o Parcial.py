print("Welcome Practica 3 2o Parcial !")# Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

def obtener_info_usuario():
    """
    Solicita al usuario su nombre, edad, dirección y número de teléfono,
    y almacena estos datos en un diccionario exclusivo.
    """
    # Crear un diccionario para almacenar la información
    info_usuario = {}

    # Solicitar información al usuario
    info_usuario['nombre'] = input("Introduce tu nombre: ")
    info_usuario['edad'] = input("Introduce tu edad: ")
    info_usuario['direccion'] = input("Introduce tu dirección: ")
    info_usuario['telefono'] = input("Introduce tu número de teléfono: ")

    return info_usuario

def mostrar_info(info):
    """
    Muestra la información del usuario en un formato estructurado.
    """
    print(f"\n{info['nombre']} tiene {info['edad']} años")
    print(f"vive en {info['direccion']}")
    print(f"su número de teléfono es {info['telefono']}.")
# Ejecutar el programa exclusivo
usuario = obtener_info_usuario()
mostrar_info(usuario)
