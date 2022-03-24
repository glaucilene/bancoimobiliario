import unittest
from main import sortear_jogadores

class TestBanco(unittest.TestCase):
    def test_checarjogadores(self):
        self.assertEqual(sortear_jogadores([1,2,3,4]), 4)

if __name__ == '__main__':
    unittest.main()