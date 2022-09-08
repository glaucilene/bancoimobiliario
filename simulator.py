from gameboard import GameBoard
from turns import Turns
import random

class Simulator():

    def __init__(self, number_players=None, number_turns=10):
        self.number_players = number_players
        self.list_players = list(range(1, self.number_players + 1))
        self.players_position = None
        self.number_turns = number_turns
        self.sort_players()
        self.create_board()

    def sort_players(self):
        if not self.players_position:
            self.players_position = random.sample(self.list_players, self.number_players)
        return self.players_position

    def create_board(self):
        self.board = GameBoard(number_positions=20)
        self.board.create_board()


    def run(self):

        print(f'Create board.\nNumber of positions: {self.board.number_positions}.\nProperty, Sale Value in position 0:{self.board.board[0].sale_value}\nProperty, Rent Value in position 0:{self.board.board[0].rent_value}')
        print(f'Players sequence: {self.players_position}')
        print('\n\n\nTurn Test.\nNumber of turns: ', self.number_turns)
        turn = Turns(number_turns=self.number_turns)
        players = turn.player_create(self.players_position)

        # TODO: preparar while para simulação
        while not turn.last_turn:
            turn.turn_control(players=players, game_board=self.board)

        print(turn.turn, turn.number_turns)
        if turn.last_turn:
            winner = turn.get_winner()
            print(f'The winner is: {winner.id}')