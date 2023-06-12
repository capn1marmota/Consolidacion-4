"""
Este módulo define la clase FileHandler, que usaremos mas adelante
"""
import csv


class FileHandler:
    """la clase FileHandler proporciona métodos estáticos para leer y escribir 
    datos en archivos csv."""
    @staticmethod
    def write_to_csv(file_name, data):
        """
        Escribe los datos proporcionados en un archivo csv.

        Args:
            file_name (str): El nombre del archivo donde se escribirán los datos.
            data (list): Una lista de listas que contienen los datos a escribir.
        """
        with open(file_name, "w", newline="",encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)

    @staticmethod
    def read_from_csv(file_name):
        """
        Lee los datos de un archivo csv.

        Args:
            file_name (str): El nombre del archivo del que se leerán los datos.

        Returns:
            data (list): Una lista de listas que contienen los datos leídos del archivo.
        """
        data = []
        with open(file_name, "r",encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data
