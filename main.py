from ctypes import sizeof
import random
# TODO: 

class GameBoard():

    def __init__(self, number_positions):
        self.number_positions = number_positions
        self.board = []
    
    def create_board(self):
        for i in range(self.number_positions):
            self.board = self.board + [Property(sale_value=10, rent_value=10)]
    

class Property():

    def __init__(self, sale_value, rent_value, owner=None):
        self.sale_value = sale_value
        self.rent_value = rent_value
        self.owner = owner
    
    def buy_property(self, player):
        self.owner = player

    def pay_rent_property(self, player, owner):
        player.money = player.money - self.rent_value
        owner.money = owner.money + self.rent_value

    def return_property(self):
        self.owner = None

class Player():

    def __init__(self, money, property):
        self.money = money
        self.property = property


class Simulator():

    def __init__(self, number_players=None):
        self.number_players = number_players

    def sort_players(self):
        list_players = [i+1 for i in range(self.number_players)]
        list_players = random.sample(list_players, self.number_players)
        return list_players
    
    def run(self):
        game_board = GameBoard(number_positions=20)
        game_board.create_board()
        print(f'Create board.\nNumber of positions: {game_board.number_positions}.\nProperty, Sale Value in position 0:{game_board.board[0].sale_value}\nProperty, Rent Value in position 0:{game_board.board[0].sale_value}')

        print(f'Players sequence: {self.sort_players()}')


class Turns():

    def __init__(self, number_turns=None, turn=None):
        self.number_turns = number_turns
        self.turn = turn

    # def turns(self, list_players):
    #     turn_control = {}
    #     for player in list_players:
    #         turn_control = {player, self.turn}
    #     return None

if __name__ == '__main__':
    Simulator(number_players=4).run()
