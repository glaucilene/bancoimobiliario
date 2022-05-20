import unittest
from main import Simulator

class TestBank(unittest.TestCase):
    def test_checkplayers(self):
        self.assertEqual(Simulator(number_players=4).sort_players(), [1,2,3,4])
    def test_turns(self):
        self.assertEqual(Simulator().turns(), None)
    def test_winner(self):
        self.assertEqual([1,1,1,1], 0)
        self.assertEqual([1,1,2,1], 2)
        self.assertEqual([1,2,1,1], 1)
        self.assertEqual([1,1,2,1], 2)
        self.assertEqual([1,1,1,2], 3)


if __name__ == '__main__':
    unittest.main()