"""
Este módulo contiene el requerimiento parte 2 del cliente
"""
from classes.particular import Particular
from classes.carga import Carga
from classes.bicicleta import Bicicleta
from classes.motocicleta import Motocicleta


def main():
    """
    Esta función crea objetos de las clases Particular, Carga, Bicicleta y Motocicleta.
    Luego imprime cada uno de estos objetos.

    Además, realiza algunas comprobaciones isinstance para demostrar la herencia y la
    relación entre las clases.
    """
    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    vehiculos = [particular, carga, bicicleta, motocicleta]

    for vehiculo in vehiculos:
        print(vehiculo)

    print(
        f"Motocicleta es instancia con relación a Particular: {isinstance(motocicleta, Particular)}"
    )
    print(
        f"Motocicleta es instancia con relación a Carga: {isinstance(motocicleta, Carga)}"
    )
    print(
        f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}"
    )
    print(
        f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}"
    )


if __name__ == "__main__":
    main()
