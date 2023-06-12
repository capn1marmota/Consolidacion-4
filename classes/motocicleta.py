from .bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, num_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios
    def __str__(self):
        return f"Marca {self.marca},Modelo {self.modelo}, {self.num_ruedas} ruedas, Tipo {self.tipo}, {self.motor} cc, Cuadro {self.cuadro}, {self.nro_radios} radios"
