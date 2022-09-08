import unittest
from turns import Turns
from player import Player

class TestPlayerCreate(unittest.TestCase):
    
    def test_none_listplayers(self):
        with self.assertRaises(ValueError):
            Turns(100).player_create(None)

    def test_empty_listplayers(self):
        with self.assertRaises(ValueError):
            Turns(100).player_create([])

    def test_correct_listplayers(self):
        ids = list(range(1, 11))
        players = Turns(100).player_create(ids)

        self.assertEqual(len(players), len(ids))
        self.assertIsInstance(players, list)
        for p in players:
            self.assertIsInstance(p, Player)
            self.assertEqual(p.money, 300)
            self.assertEqual(p.board_position, 0)
            self.assertIsNotNone(p.id)
            self.assertIn(p.id, ids)

class TestLastTurn(unittest.TestCase):
    def test_is_lastturn(self):
        turn = Turns(10)
        turn.turn = 10
        self.assertTrue(turn.last_turn)
    
    def test_is_not_lastturn(self):
        turn = Turns(10)
        turn.turn = 3
        self.assertFalse(turn.last_turn)

    def test_is_morethan_numberturns(self):
        turn = Turns(10)
        turn.turn = 1000
        self.assertTrue(turn.last_turn)

class TestGetWinner(unittest.TestCase):
    
    def test_none_with_no_player(self):
        turn = Turns(10)
        self.assertIsNone(turn.get_winner())
    
    def test_first_player_winner(self):
        turn = Turns(10)
        players = self.create_player_list()
        players[0].money = 1000
        turn.players = players
        winner = turn.get_winner()
        self.assertIsNotNone(winner)
        self.assertIsInstance(winner, Player)
        self.assertEqual(winner, players[0])
    
    def test_last_player_winner(self):
        turn = Turns(10)
        players = self.create_player_list()
        players[9].money = 1000
        turn.players = players
        winner = turn.get_winner()
        self.assertIsNotNone(winner)
        self.assertIsInstance(winner, Player)
        self.assertEqual(winner, players[9])

    def test_tied_player_winner(self):
        turn = Turns(10)
        players = self.create_player_list()
        players[0].money = 9
        turn.players = players
        winner = turn.get_winner()
        self.assertIsNotNone(winner)
        self.assertIsInstance(winner, Player)
        self.assertEqual(winner, players[1])

    def create_player_list(self):
        return [Player(money=10, board_position=i, id=i) for i in range(1, 11)]



if __name__ == '__main__':
    unittest.main()