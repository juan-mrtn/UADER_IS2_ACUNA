class Factura:
    def __init__(self, importe):
        self.importe = importe

    def mostrar(self):
        pass

class FacturaResponsable(Factura):
    def mostrar(self):
        print(f"Factura A - Importe: ${self.importe}")

class FacturaNoInscripto(Factura):
    def mostrar(self):
        print(f"Factura C - Importe: ${self.importe}")

class FacturaExento(Factura):
    def mostrar(self):
        print(f"Factura E - Importe: ${self.importe}")

class FacturaFactory:
    @staticmethod
    def crear_factura(tipo, importe):
        if tipo == "responsable":
            return FacturaResponsable(importe)
        elif tipo == "no_inscripto":
            return FacturaNoInscripto(importe)
        elif tipo == "exento":
            return FacturaExento(importe)
        else:
            raise ValueError("Tipo de factura no válido")

# Uso
factura = FacturaFactory.crear_factura("responsable", 1500)
factura.mostrar()
