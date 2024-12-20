import unittest
import Cambia_texto


class ProbarCambiaTexto(unittest.TestCase):
    def test_upper(self):
        palabra = "buen día"
        resultado = Cambia_texto.all_to_upper(palabra)
        self.assertEqual(resultado, "BUEN DÍA")


if __name__ == '__main__':
    unittest.main()
