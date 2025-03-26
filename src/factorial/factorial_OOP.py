class Factorial:
    def __init__(self):
        pass

    def calcular_factorial(self, num):
        if num < 0:
            print("El factorial de un número negativo no existe.")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, min, max):
        if min > max:
            print("El valor mínimo no puede ser mayor que el máximo.")
            return

        for i in range(min, max + 1):
            print(f"Factorial de {i} es {self.calcular_factorial(i)}")

# Ejecutar el programa
if __name__ == "__main__":
    import sys

    # Verificar si los argumentos fueron pasados
    if len(sys.argv) == 3:
        try:
            min = int(sys.argv[1])
            max = int(sys.argv[2])
            factorial_obj = Factorial()  # Crear una instancia de la clase Factorial
            factorial_obj.run(min, max)  # Llamar al método run con los valores proporcionados
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
    else:
        print("Debe proporcionar dos argumentos: mínimo y máximo.")
