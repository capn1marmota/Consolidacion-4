from .automovil import Automovil

class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, peso):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.peso = peso
    def __str__(self):
        return f"Marca {self.marca},Modelo {self.modelo}, {self.num_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc, Peso {self.peso}"
