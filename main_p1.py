"""
Este módulo contiene el requerimiento parte 1 del cliente
"""
from classes.automovil import Automovil


def solicitar_datos_automovil():
    """
    Solicita al usuario los datos de un automóvil y crea un objeto Automovil con ellos.

    Los datos solicitados son: marca, modelo, número de ruedas, velocidad y cilindrada.

    Returns:
        Automovil: Un objeto Automovil creado con los datos proporcionados por el usuario.
    """
    marca = input("Inserte la marca del automóvil: ")
    modelo = input("Inserte el modelo: ")
    num_ruedas = int(input("Inserte el número de ruedas: "))
    velocidad = int(input("Inserte la velocidad en km/h: "))
    cilindrada = int(input("Inserte el cilindraje en cc: "))
    return Automovil(marca, modelo, num_ruedas, velocidad, cilindrada)


def main():
    """
    Solicita al usuario el número de automóviles a insertar, luego recopila los datos para cada uno
    y los guarda en una lista. Finalmente, imprime los datos de todos los automóviles.
    """
    num_automoviles = int(input("Cuantos Vehiculos desea insertar: "))
    automoviles = []

    for i in range(num_automoviles):
        print(f"Datos del automóvil {i+1}")
        auto = solicitar_datos_automovil()
        automoviles.append(auto)

    print("Imprimiendo por pantalla los Vehículos:")
    for i, auto in enumerate(automoviles, start=1):
        print(
            f"Datos del automóvil {i} : Marca {auto.marca}, Modelo {auto.modelo}, {auto.num_ruedas} ruedas, {auto.velocidad} Km/h, {auto.cilindrada} cc"
        )


if __name__ == "__main__":
    main()
