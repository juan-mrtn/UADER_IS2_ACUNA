# ------------------------------------------
# Copyright UADER-FCyT-iS2©2025 todos los derechos reservados
# 
# Descripción: Recupera valores desde archivos JSON usando Branching by Abstraction
# - Implementación nueva: Singleton con mejor manejo de errores
# - Implementación vieja: funciones originales
# Versión: 1.2
# ------------------------------------------

import json
import sys
import argparse

# Flag para cambiar entre implementaciones (True = nueva, False = vieja)
USE_NEW_VERSION = True

# ===================== VERSIÓN VIEJA =====================
def obtener_valor(archivo_json, clave="token1"):
    try:
        # Abrir y leer el contenido del archivo JSON
        with open(archivo_json, 'r') as archivo:
            contenido = archivo.read()
        datos = json.loads(contenido)

        # Buscar la clave en el diccionario
        if clave in datos:
            print(f"Valor de '{clave}': {datos[clave]}")
        else:
            print(f"Clave '{clave}' no encontrada en el archivo.")
    except FileNotFoundError:
        print(f"Archivo '{archivo_json}' no encontrado.")
    except json.JSONDecodeError:
        print("El archivo no contiene un JSON válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

# ===================== VERSIÓN NUEVA (Singleton) =====================
class JSONHandler:
    """
    Clase Singleton para manejo de archivos JSON
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_value(self, json_file, key="token1"):
        """
        Obtiene valor de clave en archivo JSON con manejo de errores
        """
        try:
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            if key in data:
                print(f"Valor de '{key}': {data[key]}")
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
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            return None

#  BRANCHING BY ABSTRACTION 
class JSONBranching:
    def __init__(self):
        if USE_NEW_VERSION:
            self.handler = JSONHandler()
        else:
            self.handler = None
    
    def obtener_valor(self, archivo_json, clave):
        if USE_NEW_VERSION:
            return self.handler.get_value(archivo_json, clave)
        else:
            return obtener_valor(archivo_json, clave)

# ===================== MAIN (cambios mínimos) =====================
def main():
    parser = argparse.ArgumentParser(
        description='Recupera el valor de una clave desde un archivo JSON',
        epilog='Copyright UADER-FCyT-iS2©2024'
    )
    parser.add_argument('archivo', help="Ruta al archivo JSON")
    parser.add_argument('--clave', default="token1", help="Clave a buscar (default: token1)")
    parser.add_argument('-v', '--version', action='store_true', help="Mostrar versión")

    args = parser.parse_args()

    if args.version:
        print("Versión 1.1")
        sys.exit(0)

    # Usamos la abstracción Branching para elegir implementación
    branching = JSONBranching()
    branching.obtener_valor(args.archivo, args.clave)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario")
        sys.exit(1)