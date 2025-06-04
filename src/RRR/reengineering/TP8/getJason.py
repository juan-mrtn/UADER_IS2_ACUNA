# ------------------------------------------
# Copyright UADER-FCyT-iS2©2025 todos los derechos reservados
# 
# Descripción: Sistema de procesamiento de pagos automatizado
# - Implementa Cadena de Responsabilidad e Iterator
# - Integra Singleton para lectura de tokens
# Versión: 1.3
# ------------------------------------------

# pylint: disable=invalid-name
"""
Módulo para procesamiento de pagos automatizado.
"""

import json
import sys
import argparse
from datetime import datetime

# Flag para cambiar entre implementaciones (True = nueva, False = vieja)
USE_NEW_VERSION = True

# ===================== VERSIÓN VIEJA =====================
def obtener_valor(archivo_json, clave="token1"):
    """Obtiene valor de una clave en archivo JSON (implementación antigua)."""
    try:
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        datos = json.loads(contenido)

        if clave in datos:
            print(f"Valor de '{clave}': {datos[clave]}")
        else:
            print(f"Clave '{clave}' no encontrada en el archivo.")
    except FileNotFoundError:
        print(f"Archivo '{archivo_json}' no encontrado.")
    except json.JSONDecodeError:
        print("El archivo no contiene un JSON válido.")
    except Exception as e:  # pylint: disable=broad-except
        print(f"Error inesperado: {e}")

# ===================== VERSIÓN NUEVA (Singleton) =====================
class JSONHandler:
    """Clase Singleton para manejo de archivos JSON."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_all_banks(self, json_file: str) -> dict:
        """Obtiene dinámicamente todos los bancos del JSON"""
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data.get("bancos", {})
        except Exception as e:  # pylint: disable=broad-except
            print(f"Error leyendo bancos: {str(e)}")
            return {}

    def get_value(self, json_file, key="token1"):
        """Obtiene valor de clave en archivo JSON con manejo de errores."""
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            # Verifica si la clave existe en el JSON
            if key in data:
                return data[key]
            print(f"Clave '{key}' no encontrada")
            return None

        except FileNotFoundError:
            print(f"Error: Archivo '{json_file}' no encontrado")
            return None
        except json.JSONDecodeError:
            print("Error: Archivo JSON inválido")
            return None
        except PermissionError:
            print("Error: Sin permisos para leer el archivo")
            return None
        except Exception as e:  # pylint: disable=broad-except
            print(f"Error inesperado: {str(e)}")
            return None

# ===================== IMPLEMENTACIÓN DE PAGOS =====================
class Payment:
    """Representa un pago procesado."""
    def __init__(self, request_id: int, token: str, amount: float):
        self.request_id = request_id
        self.token = token
        self.amount = amount
        self.timestamp = datetime.now()

    def to_dict(self) -> dict:
        """Convierte el pago a diccionario para serialización."""
        return {
            "id": self.request_id,
            "token": self.token,
            "amount": self.amount,
            "timestamp": self.timestamp.isoformat()
        }

    def __str__(self) -> str:
        """Representación legible del pago."""
        return f"Pago #{self.request_id} via {self.token}: ${self.amount}"

class PaymentHandler:
    """Manejador de pagos para una cuenta específica."""
    def __init__(self, token: str, balance: float, next_handler=None):
        self.token = token
        self.balance = balance
        self.next_handler = next_handler

    def process_payment(self, request_id: int, amount: float) -> Payment:
        """Intenta procesar el pago en esta cuenta o pasa al siguiente manejador."""
        if self.balance >= amount:
            self.balance -= amount
            return Payment(request_id, self.token, amount)

        if self.next_handler:
            return self.next_handler.process_payment(request_id, amount)

        return None

    def get_balance(self) -> float:
        """Obtiene el saldo actual."""
        return self.balance

    def can_process(self, amount: float) -> bool:
        """Verifica si puede procesar un monto."""
        return self.balance >= amount

class PaymentProcessor:
    """Sistema de procesamiento de pagos con Cadena de Responsabilidad."""
    def __init__(self):
        self.handlers = None
        self.payments = []
        self.request_counter = 0

    def setup_handlers(self, bancos: dict):
        """Configura la cadena de manejadores con token1 como primer eslabón."""
        if not bancos:
            raise ValueError("No se encontraron bancos en el JSON")

        # Ordenar tokens por saldo (mayor a menor)
        sorted_tokens = sorted(
            bancos.items(),
            key=lambda x: x[1]["saldo_inicial"],
            reverse=True
        )

        # Construir cadena de responsabilidad
        previous_handler = None
        for token, data in sorted_tokens:
            handler = PaymentHandler(
                token=token,
                balance=data["saldo_inicial"],
                next_handler=previous_handler
            )
            previous_handler = handler
        self.handlers = previous_handler  # El último handler es el primero en la cadena

    def make_payment(self, amount: float) -> Payment:
        """Ejecuta un pago a través de la cadena de responsabilidad."""
        self.request_counter += 1
        payment = self.handlers.process_payment(self.request_counter, amount)

        if payment:
            self.payments.append(payment)
            print(f"Pago {payment.request_id} procesado con {payment.token}")
            return payment

        print(f"Error en pago {self.request_counter}: Saldo insuficiente")
        return None

    def list_payments(self):
        """Iterator para listar pagos en orden cronológico."""
        return iter(sorted(self.payments, key=lambda p: p.timestamp))

#BRANCHING BY ABSTRACTION 
class JSONBranching:
    """Facade para seleccionar implementación JSON."""
    def __init__(self):
        if USE_NEW_VERSION:
            self.handler = JSONHandler()
        else:
            self.handler = None

    def obtener_valor(self, archivo_json, clave):
        """Obtiene valor usando implementación seleccionada."""
        if USE_NEW_VERSION:
            return self.handler.get_value(archivo_json, clave)

        return obtener_valor(archivo_json, clave)

    def get_handler_type(self) -> str:
        """Devuelve el tipo de handler en uso."""
        return "Singleton" if USE_NEW_VERSION else "Funciones"

# ===================== MAIN ACTUALIZADO =====================
def main():
    """Función principal del programa."""
    parser = argparse.ArgumentParser(
        description='Sistema de procesamiento de pagos automatizado',
        epilog='Copyright UADER-FCyT-iS2©2024'
    )
    parser.add_argument('archivo', help="Ruta al archivo JSON con tokens")
    parser.add_argument('--clave', default="token1", help="Clave a buscar (default: token1)")
    parser.add_argument('-p', '--pagos', type=int, default=5, help="Número de pagos a procesar")
    parser.add_argument('-v', '--version', action='store_true', help="Mostrar versión")
    parser.add_argument('-l', '--listar', action='store_true', help="Listar pagos realizados")

    args = parser.parse_args()

    if args.version:
        print("Versión 1.2")
        sys.exit(0)

    # Modo procesamiento de pagos
    if args.pagos > 0:
        #Configura la cadena dinámicamente con todos los bancos
        json_handler = JSONHandler()
        bancos = json_handler.get_all_banks(args.archivo)

        processor = PaymentProcessor()
        processor.setup_handlers(bancos)

        # Procesar pagos
        for _ in range(args.pagos):
            processor.make_payment(500.0)

    # Listar pagos si se solicita
    if args.listar:
        if 'processor' in locals() and processor.payments:
            print("\n Historial de pagos:")
            for i, payment in enumerate(processor.list_payments()):
                print(f"{i+1}. [{payment.timestamp}] {payment.token} - ${payment.amount}")
        else:
            print("\n No hay pagos para listar")

    # Modo original (obtener valor) si no se procesaron pagos
    elif args.pagos <= 0:
        branching = JSONBranching()
        branching.obtener_valor(args.archivo, args.clave)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario")
        sys.exit(1)
"""
Resultados de pylint:
"""
"""
juanacuna@MacBook-de-Juan TP8 % pylint getJason.py
************* Module getJason
getJason.py:3:1: C0303: Trailing whitespace (trailing-whitespace)
getJason.py:181:25: C0303: Trailing whitespace (trailing-whitespace)

------------------------------------------------------------------
Your code has been rated at 9.86/10 (previous run: 9.73/10, +0.14)"""