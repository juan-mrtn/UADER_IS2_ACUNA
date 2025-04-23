class CalculadoraImpuestos:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CalculadoraImpuestos, cls).__new__(cls)
        return cls._instance

    def calcular(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones = base_imponible * 0.012
        return iva + iibb + contribuciones

# Uso
imp = CalculadoraImpuestos().calcular(1000)
print(f"Impuestos: ${imp:.2f}")

