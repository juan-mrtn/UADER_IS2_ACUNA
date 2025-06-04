import os
import sys

class Rango:
    def __init__(self, args):
        try:
            if len(args) == 1:
                self.lower = 1
                self.upper = 50
            elif len(args) == 2:
                self.lower = 1
                self.upper = int(args[1])
            else:
                self.lower = int(args[1])
                self.upper = int(args[2])
        except ValueError:
            print('Argumentos inválidos')
            sys.exit()

    def es_valido(self):
        return self.lower <= self.upper

class CalculadoraPrimos:
    def __init__(self, rango):
        self.rango = rango

    def es_primo(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    def mostrar_primos(self):
        print(f'Números primos entre {self.rango.lower} y {self.rango.upper} son:\n')
        for num in range(self.rango.lower, self.rango.upper + 1):
            if self.es_primo(num):
                print(f'{num} ', end='')
        print()

def main():
    os.system('clear')
    rango = Rango(sys.argv)

    if not rango.es_valido():
        print('El rango es inválido')
        sys.exit()

    calculadora = CalculadoraPrimos(rango)
    calculadora.mostrar_primos()

if __name__ == "__main__":
    main()
