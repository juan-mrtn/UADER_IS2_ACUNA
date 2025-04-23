class Hamburguesa:
    def entregar(self, metodo):
        print(f"Hamburguesa entregada por: {metodo}")

# Uso
pedido = Hamburguesa()
pedido.entregar("mostrador")
pedido.entregar("retirada")
pedido.entregar("delivery")

