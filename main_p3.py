"""
Este archivo contiene el requerimiento parte 3 del cliente
"""
from file_handler import FileHandler
from classes.particular import Particular
from classes.carga import Carga
from classes.bicicleta import Bicicleta
from classes.motocicleta import Motocicleta


def guardar_datos_csv():
    """
    Esta función recolecta los datos de varios objetos vehiculo y los guarda en un archivo CSV.

    Primero, llama al método guardar_datos_csv de varios objetos vehiculo para obtener sus datos en 
    el formato adecuado.
    Luego, llama al método write_to_csv de la clase FileHandler para escribir estos datos en un 
    archivo CSV.

    Si ocurre alguna excepción durante este proceso, como un FileNotFoundError o un PermissionError,
    la función maneja estas excepciones e imprime un mensaje de error apropiado.
    """
    try:
        vehiculos = [
            particular.guardar_datos_csv(),
            carga.guardar_datos_csv(),
            bicicleta.guardar_datos_csv(),
            motocicleta.guardar_datos_csv(),
        ]
        FileHandler.write_to_csv("vehiculos.csv", vehiculos)
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except PermissionError:
        print("No se tienen los permisos necesarios para escribir en el archivo.")


def cargar_datos_csv():
    """
    Esta función lee los datos de un archivo CSV y los imprime.

    Primero, llama al método read_from_csv de la clase FileHandler para leer los datos del 
    archivo CSV.
    Luego, recorre estos datos e imprime cada vehiculo en una línea separada.

    Si ocurre alguna excepción durante este proceso, como un FileNotFoundError o un PermissionError,
    la función maneja estas excepciones e imprime un mensaje de error apropiado.
    """
    try:
        vehiculos = FileHandler.read_from_csv("vehiculos.csv")
        for vehiculo in vehiculos:
            print(f"Lista de Vehiculos {vehiculo[0]}")
            print(vehiculo[1])
    except FileNotFoundError:
        print("El archivo no fue encontrado.")
    except PermissionError:
        print("No se tienen los permisos necesarios para leer el archivo.")


particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

guardar_datos_csv()
cargar_datos_csv()
