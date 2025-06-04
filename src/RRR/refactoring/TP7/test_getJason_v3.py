import unittest
import json
import os
from unittest.mock import patch, mock_open
from getJason_v2 import JSONHandler, obtener_valor, JSONBranching

# Cargar datos REALES del archivo JSON
def load_test_tokens():
    with open('sitedata.json', 'r') as f:
        return json.load(f)

# Solo cargar datos si el archivo existe
if os.path.exists('sitedata.json'):
    REAL_TOKENS = load_test_tokens()
    REAL_JSON_STR = json.dumps(REAL_TOKENS)
else:
    raise FileNotFoundError("No se encontró sitedata.json para las pruebas")

class TestJSONHandler(unittest.TestCase):
    """Pruebas para la implementación nueva (Singleton)"""
    
    @patch('builtins.open', mock_open(read_data=REAL_JSON_STR))
    def test_get_existing_key(self):
        """Obtener valor de clave existente usando datos reales"""
        handler = JSONHandler()
        for token, value in REAL_TOKENS.items():
            with self.subTest(token=token):
                result = handler.get_value("sitedata.json", token)
                self.assertEqual(result, value)
    
    @patch('builtins.open', mock_open(read_data=REAL_JSON_STR))
    def test_get_non_existing_key(self):
        """Clave no existente debe retornar None"""
        handler = JSONHandler()
        result = handler.get_value("sitedata.json", "token_inexistente")
        self.assertIsNone(result)

class TestBranching(unittest.TestCase):
    """Prueba la capa de abstracción con datos reales"""
    
    @patch('builtins.open', mock_open(read_data=REAL_JSON_STR))
    def test_both_versions(self):
        """Verifica que ambas versiones funcionen con datos reales"""
        for version in [True, False]:
            with self.subTest(version=version), \
                 patch('getJason_v2.USE_NEW_VERSION', version):
                
                branching = JSONBranching()
                from io import StringIO
                from contextlib import redirect_stdout
                
                for token, expected_value in REAL_TOKENS.items():
                    f = StringIO()
                    with redirect_stdout(f):
                        branching.obtener_valor("sitedata.json", token)
                    
                    output = f.getvalue().strip()
                    self.assertIn(expected_value, output)

if __name__ == '__main__':
    unittest.main()