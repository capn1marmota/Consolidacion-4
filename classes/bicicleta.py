from .vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo = tipo
    def __str__(self):
        return f"Marca {self.marca},Modelo {self.modelo}, {self.num_ruedas} ruedas, Tipo {self.tipo}"
