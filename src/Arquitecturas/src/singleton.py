class FactorialCalculator:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FactorialCalculator, cls).__new__(cls)
        return cls._instance

    def calcular(self, n):
        if n == 0 or n == 1:
            return 1
        return n * self.calcular(n - 1)

# Uso
calc1 = FactorialCalculator()
calc2 = FactorialCalculator()
print(calc1 is calc2)  # True
print(calc1.calcular(5))  # 120
