import unittest
from main import Simulador

class TestBanco(unittest.TestCase):
    def test_checarjogadores(self):
        self.assertEqual(Simulador(numero_jogadores=4).sortear_jogadores(), [1,2,3,4])

if __name__ == '__main__':
    unittest.main()