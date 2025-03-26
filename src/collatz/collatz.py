import matplotlib.pyplot as plt
import numpy as np

def collatz_iterations(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

start_numbers = []
iterations = []

for n in range(1, 10001):
    start_numbers.append(n)
    iterations.append(collatz_iterations(n))

start_numbers = np.array(start_numbers)
iterations = np.array(iterations)

plt.figure(figsize=(10, 6))
plt.scatter(iterations, start_numbers, color='blue', alpha=0.5, s=10)
plt.title("Número de Iteraciones de la Conjetura de Collatz")
plt.xlabel("Número de Iteraciones")
plt.ylabel("Número de Inicio de la Secuencia (n)")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(iterations, start_numbers, color='blue', alpha=0.5, s=10)
plt.title("Número de Iteraciones de la Conjetura de Collatz")
plt.xlabel("Número de Iteraciones")
plt.ylabel("Número de Inicio de la Secuencia (n)")
plt.grid(True)
plt.savefig("collatz_iterations.png")
