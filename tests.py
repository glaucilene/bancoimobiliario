import unittest
from main import Simulator

class TestBank(unittest.TestCase):
    def setUp(self):
        self.simulator = Simulator(number_players=4)
        self.players_position = self.simulator.sort_players()
    
    def test_list_players(self):
        self.assertListEqual(self.simulator.list_players, [1,2,3,4])

    def test_sort_players(self):
        self.assertEqual(len(list(set(self.simulator.players_position))), self.simulator.number_players)
    
    def test_order_player(self):
        '''
            Testa se o sorteio de jogadores retorna a lista sorteada inicialmente
        '''
        self.simulator.sort_players()
        self.assertListEqual(self.players_position, self.simulator.players_position)
    
    # def test_checkplayers(self):
    #     self.assertEqual(Simulator(number_players=4).sort_players(), [1,2,3,4])
    # def test_turns(self):
    #     self.assertEqual(Simulator().turns(), None)
    # def test_winner(self):
    #     self.assertEqual([1,1,1,1], 0)
    #     self.assertEqual([1,1,2,1], 2)
    #     self.assertEqual([1,2,1,1], 1)
    #     self.assertEqual([1,1,2,1], 2)
    #     self.assertEqual([1,1,1,2], 3)


if __name__ == '__main__':
    unittest.main()