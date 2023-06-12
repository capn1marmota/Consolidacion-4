from .automovil import Automovil

class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindrada, puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindrada)
        self.puestos = puestos
    def __str__(self):
        return f"Marca {self.marca},Modelo {self.modelo}, {self.num_ruedas} ruedas, {self.velocidad} Km/h, {self.cilindrada} cc, Puestos{self.puestos}"
