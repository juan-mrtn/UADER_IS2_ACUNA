"""El patrón Abstract Factory permite crear familias de objetos relacionados sin
especificar sus clases concretas. En el ejemplo, se simula la construcción de
una interfaz gráfica para dos sistemas operativos diferentes: Windows y Mac. 
Cada sistema tiene su propia fábrica (UIFactoryWindows, UIFactoryMac) que sabe
cómo crear sus respectivos botones y menús (BotonWindows, MenuMac, etc.). 
El cliente (construir_ui) utiliza la fábrica sin conocer los detalles de implementación, 
lo que permite cambiar completamente el estilo de la interfaz simplemente cambiando la 
fábrica usada. Este patrón es útil cuando se necesita asegurar la coherencia entre 
productos de una misma "familia", como en interfaces multiplataforma."""

# Interfaces
class Boton:
    def mostrar(self): pass

class Menu:
    def mostrar(self): pass

# Fábrica concreta 1
class UIFactoryWindows:
    def crear_boton(self): return BotonWindows()
    def crear_menu(self): return MenuWindows()

# Fábrica concreta 2
class UIFactoryMac:
    def crear_boton(self): return BotonMac()
    def crear_menu(self): return MenuMac()

# Productos concretos
class BotonWindows(Boton):
    def mostrar(self): print("Botón de Windows")

class MenuWindows(Menu):
    def mostrar(self): print("Menú de Windows")

class BotonMac(Boton):
    def mostrar(self): print("Botón de Mac")

class MenuMac(Menu):
    def mostrar(self): print("Menú de Mac")

# Cliente
def construir_ui(factory):
    boton = factory.crear_boton()
    menu = factory.crear_menu()
    boton.mostrar()
    menu.mostrar()

# Uso
construir_ui(UIFactoryWindows())
construir_ui(UIFactoryMac())
