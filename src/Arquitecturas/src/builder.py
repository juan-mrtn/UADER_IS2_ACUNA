class Avion:
    def __init__(self):
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def mostrar(self):
        print("Avión construido con:", ", ".join(self.partes))

class AvionBuilder:
    def construir(self):
        avion = Avion()
        avion.agregar_parte("body")
        avion.agregar_parte("turbina izquierda")
        avion.agregar_parte("turbina derecha")
        avion.agregar_parte("ala izquierda")
        avion.agregar_parte("ala derecha")
        avion.agregar_parte("tren de aterrizaje")
        return avion

# Uso
builder = AvionBuilder()
avion = builder.construir()
avion.mostrar()
