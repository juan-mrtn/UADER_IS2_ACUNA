import copy

class Prototipo:
    def clonar(self):
        return copy.deepcopy(self)

class Documento(Prototipo):
    def __init__(self, contenido):
        self.contenido = contenido

# Uso
doc1 = Documento("Texto original")
doc2 = doc1.clonar()
doc3 = doc2.clonar()

print(doc1.contenido, doc2.contenido, doc3.contenido)
