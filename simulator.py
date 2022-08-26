from gameboard import GameBoard
from turns import Turns
import random

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
        print(f'Create board.\nNumber of positions: {game_board.number_positions}.\nProperty, Sale Value in position 0:{game_board.board[0].sale_value}\nProperty, Rent Value in position 0:{game_board.board[0].rent_value}')

        list_position_players = self.sort_players()

        print(f'Players sequence: {list_position_players}')

        number_turns = 2
        print('\n\n\nTurn Test.\nNumber of turns: ', number_turns)
        turn = Turns(number_turns=number_turns)
        players = turn.player_create(list_position_players)

        # TODO: preparar while para simulação
        while turn.turn <= number_turns:
            turn.turn_control(players=players, game_board=game_board)

            if turn.turn == 2:
                greater_balance = 0
                winner = None
                for player in players:
                    if player.money > greater_balance:
                        greater_balance = player.money
                        winner = player
                print(f'O ganhador foi o jogador:{winner.id}')
                break