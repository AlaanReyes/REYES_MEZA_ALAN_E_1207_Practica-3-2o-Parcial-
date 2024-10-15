print("Welcome Practica 3 2o Parcial !")# Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

# Diccionario de divisas
divisas = {
    'EURO': '€',
    'DOLAR': '$',
    'YEN': '¥'
}

def buscar_divisa():
    """
    Esta función permite al usuario buscar el símbolo de una divisa.
    El usuario puede ingresar el nombre de la divisa o escribir 'salir' para terminar el programa.
    """
    while True:
        # Solicitar al usuario que ingrese una divisa
        divisa_input = input("Introduce una divisa (Euro, Dollar, Yen) o escribe 'salir' para terminar: ").strip().upper()

        # Opcion para salir del programa
        if divisa_input == 'SALIR':
            print("GRACIAS POR USAR MI PROGRAMA")
            break

        # Buscar el simbolo de la divisa en el diccionario
        simbolo = divisas.get(divisa_input)

        # Mostrar el resultado al usuario
        if simbolo:
            print(f"El símbolo de {divisa_input.capitalize()} es: {simbolo}")
        else:
            print("La divisa no está en el diccionario.")

# Llamar a la funcion para iniciar el programa
buscar_divisa()
