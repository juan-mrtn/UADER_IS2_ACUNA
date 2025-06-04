import unittest
import json
from unittest.mock import patch, mock_open
from getJason_v2 import JSONHandler, obtener_valor, JSONBranching

# Datos del archivo sitedata.json proporcionado
TEST_JSON_DATA = {
    "token1": "C598-ECF9-F0F7-881A",
    "token2": "C598-ECF9-F0F7-881B"
}
JSON_STR = json.dumps(TEST_JSON_DATA)

class TestJSONHandler(unittest.TestCase):
    """Pruebas para la implementación nueva (Singleton)"""
    
    def test_singleton_instance(self):
        """Verifica que solo exista una instancia del Singleton"""
        handler1 = JSONHandler()
        handler2 = JSONHandler()
        self.assertIs(handler1, handler2)
    
    @patch('builtins.open', mock_open(read_data=JSON_STR))
    def test_get_existing_key(self):
        """Obtener valor de clave existente"""
        handler = JSONHandler()
        result = handler.get_value("sitedata.json", "token1")
        self.assertEqual(result, "C598-ECF9-F0F7-881A")
    
    @patch('builtins.open', mock_open(read_data=JSON_STR))
    def test_get_non_existing_key(self):
        """Clave no existente debe retornar None"""
        handler = JSONHandler()
        result = handler.get_value("sitedata.json", "token3")
        self.assertIsNone(result)

class TestLegacyImplementation(unittest.TestCase):
    """Pruebas para la implementación vieja (funciones)"""
    
    @patch('builtins.open', mock_open(read_data=JSON_STR))
    def test_obtener_valor_existente(self):
        """Prueba la función original con clave existente"""
        from io import StringIO
        from contextlib import redirect_stdout
        
        f = StringIO()
        with redirect_stdout(f):
            obtener_valor("sitedata.json", "token1")
        
        output = f.getvalue().strip()
        self.assertIn("C598-ECF9-F0F7-881A", output)
    
    @patch('builtins.open', mock_open(read_data=JSON_STR))
    def test_obtener_valor_inexistente(self):
        """Prueba la función original con clave no existente"""
        from io import StringIO
        from contextlib import redirect_stdout
        
        f = StringIO()
        with redirect_stdout(f):
            obtener_valor("sitedata.json", "token3")
        
        output = f.getvalue().strip()
        self.assertIn("no encontrada", output)

class TestBranching(unittest.TestCase):
    """Prueba la capa de abstracción"""
    
    @patch('builtins.open', mock_open(read_data=JSON_STR))
    def test_branching_new_version(self):
        """Verifica que use correctamente la nueva versión"""
        with patch('getJason_v2.USE_NEW_VERSION', True):  # Forzar nueva versión
            branching = JSONBranching()
            
            from io import StringIO
            from contextlib import redirect_stdout
            
            f = StringIO()
            with redirect_stdout(f):
                branching.obtener_valor("sitedata.json", "token1")
            
            output = f.getvalue().strip()
            self.assertIn("C598-ECF9-F0F7-881A", output)
    
    @patch('builtins.open', mock_open(read_data=JSON_STR))
    def test_branching_old_version(self):
        """Verifica que use correctamente la versión vieja"""
        with patch('getJason_v2.USE_NEW_VERSION', False):  # Forzar versión vieja
            branching = JSONBranching()
            
            from io import StringIO
            from contextlib import redirect_stdout
            
            f = StringIO()
            with redirect_stdout(f):
                branching.obtener_valor("sitedata.json", "token1")
            
            output = f.getvalue().strip()
            self.assertIn("C598-ECF9-F0F7-881A", output)

if __name__ == '__main__':
    unittest.main()