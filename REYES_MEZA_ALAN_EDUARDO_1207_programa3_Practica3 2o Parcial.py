print("Welcome Practica 3 2o Parcial !")# Mensaje de bienvenida al usuario
print(" ")
print("REYES MEZA ALAN EDUARDO_1207 :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO

frutas = {'Platano': 30, 'Manzana': 37, 'Pera': 10, 'Naranja': 25, 'Fresa': 50,'Mango': 32, 'Sandia': 34, 'Uva': 16}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, 'pesos mexicanos')
else: 
    print("Una disculpa, la fruta", fruta, "no esta en nuestro menu")
