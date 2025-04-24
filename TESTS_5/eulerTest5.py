import unittest
from metodo_euler import metodo_euler, f

class TestMetodoEuler(unittest.TestCase):
    def test_n4(self):
        # Caso proporcionado en el código (n=4)
        result = metodo_euler(f, t0=2, y0=1, tn=3, n=4)
        self.assertAlmostEqual(result, 2.85075224, places=6)

    def test_n1(self):
        # Caso con n=1 (para validar el cálculo con un paso grande)
        result = metodo_euler(f, t0=2, y0=1, tn=3, n=1)
        self.assertAlmostEqual(result, 4.0, places=6)

    def test_n2(self):
        # Caso con n=2 (validación intermedia)
        result = metodo_euler(f, t0=2, y0=1, tn=3, n=2)
        self.assertAlmostEqual(result, 3.1953125, places=6)

    def test_n0_division_by_zero(self):
        # Verifica que se lance una excepción si n=0
        with self.assertRaises(ZeroDivisionError):
            metodo_euler(f, t0=2, y0=1, tn=3, n=0)

if __name__ == '__main__':
    unittest.main()