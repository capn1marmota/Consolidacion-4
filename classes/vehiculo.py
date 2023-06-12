class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.num_ruedas = num_ruedas
    def __str__(self):
        return f"Marca {self.marca},Modelo {self.modelo}, {self.num_ruedas} ruedas"
    def guardar_datos_csv(self):
        """
    Guarda los datos del vehículo
    Los datos se guardan en el formato [nombre de la clase, diccionario de atributos del vehículo].
    """
        return [str(self.__class__), self.__dict__]
