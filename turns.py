from player import Player
import random
import logging as log

class Turns():

    def __init__(self, number_turns):
        self.number_turns = number_turns
        self.turn = 0
        self.players = []


    @property
    def last_turn(self):
        return self.turn >= self.number_turns

    def get_winner(self):
        greater_balance = 0
        winner = None
        for player in self.players:
            if player.money > greater_balance:
                greater_balance = player.money
                winner = player
        return winner

    def player_create(self, list_players):

        if not list_players : raise ValueError('list_players should be filled')

        players = []
        for player_id in list_players:
            player = Player(money=300, board_position=0, id=player_id)
            players.append(player)
    
        log.debug('List object players: ', players)
        
        self.players = players
        return self.players

    def roll_dice(self):
        return random.randint(1, 6)

    def player_walks(self, player, game_board, dice_result ):
        if (player.board_position + dice_result) >= game_board.number_positions:
            new_dice = abs((player.board_position + dice_result) - game_board.number_positions)
            player.board_position = new_dice
        else:
            player.board_position += dice_result
    
    def deal_property(self, player, game_board):
        if game_board.board[player.board_position].return_property() != None:
            game_board.board[player.board_position].pay_rent_property(player=player, owner=game_board.board[player.board_position].owner)
        else:
            game_board.board[player.board_position].buy_property(player=player)


    def turn_control(self, players, game_board):
        # (Na jogada 1000 jogador com maior saldo ganha) - critério desempate é ordem dos jogadores
        self.turn = self.turn + 1
        # TODO: poderia verificar se tem nova lista de jogadores - Checar onde por
        for player in players:
            dice_result = self.roll_dice()
            self.player_walks(player=player, game_board=game_board, dice_result=dice_result)    
            self.deal_property(player=player, game_board=game_board)
