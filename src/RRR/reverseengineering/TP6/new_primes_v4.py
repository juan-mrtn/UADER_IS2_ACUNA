import os
import sys

# Constante que define el valor máximo permitido
MAX_VALOR = 65535

# Clase que representa un rango de números
class Rango:
    def __init__(self, args):
        try:
            # Si no se pasan argumentos, se usa el rango por defecto (1 a 50)
            if len(args) == 1:
                self.lower = 1
                self.upper = 50
            # Si se pasa un solo argumento, es el límite superior (desde 1)
            elif len(args) == 2:
                self.lower = 1
                self.upper = int(args[1])
            # Si se pasan dos argumentos, son límite inferior y superior
            else:
                self.lower = int(args[1])
                self.upper = int(args[2])
        except ValueError:
            print('Argumentos inválidos')
            sys.exit()

    # Valida que el rango sea correcto
    def es_valido(self):
        if self.lower < 0 or self.upper < 0:
            print('Error: No se permiten números negativos.')
            return False
        if self.lower > MAX_VALOR or self.upper > MAX_VALOR:
            print(f'Error: No se permiten valores mayores a {MAX_VALOR}.')
            return False
        if self.lower > self.upper:
            print('Error: El rango es inválido.')
            return False
        return True

# Clase que calcula y muestra los números primos en un rango
class CalculadoraPrimos:
    def __init__(self, rango):
        self.rango = rango

    # Verifica si un número es primo
    def es_primo(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5)+1):  # Optimización: hasta la raíz cuadrada
            if num % i == 0:
                return False
        return True

    # Muestra por pantalla los primos en el rango dado
    def mostrar_primos(self):
        print(f'Números primos entre {self.rango.lower} y {self.rango.upper} son:\n')
        for num in range(self.rango.lower, self.rango.upper + 1):
            if self.es_primo(num):
                print(f'{num} ', end='')  # Imprime en la misma línea
        print()  # Salto de línea final

# Función principal del programa
def main():
    os.system('clear')  # Limpia la consola (solo en sistemas tipo Unix)
    rango = Rango(sys.argv)  # Crea el rango a partir de los argumentos

    if not rango.es_valido():  # Verifica si el rango es válido
        sys.exit()

    calculadora = CalculadoraPrimos(rango)  # Crea la calculadora de primos
    calculadora.mostrar_primos()  # Ejecuta el cálculo y muestra los resultados

# Punto de entrada del script
if __name__ == "__main__":
    main()
