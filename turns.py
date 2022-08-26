from player import Player
import random

class Turns():

    def __init__(self, number_turns):
        self.number_turns = number_turns
        self.turn = 0

    def player_create(self, list_players):
        players = []
        if self.turn == 0:
            for player_id in list_players:
                player = Player(money=300, board_position=0, id=player_id)
                players.append(player)
        
        print('List object players: ', players)
        for player in players:
            print('Player ID: ', player.id)

        return players

    
    def turn_control(self, players, game_board):
        # (Na jogada 1000 jogador com maior saldo ganha) - critério desempate é ordem dos jogadores
        print('\n\n\n\nActual turn: ', self.turn)
        self.turn = self.turn + 1
        print('Turn increment, new value: ', self.turn)
        # TODO: poderia verificar se tem nova lista de jogadores - Checar onde por
        print('Now, loop list player')
        for player in players:
            print('\nPlayer id: ', player.id)
            die_result = random.randint(1, 6)
            print('Die result: ', die_result)
            print('Player position before: ', player.board_position)
            if (player.board_position + die_result) > 20:
                new_die = (player.board_position + die_result) - 20
                player.board_position = new_die
                print('Player position after verif end board, new position: ', player.board_position)
            else:
                player.board_position += die_result
                print('New Player position: ', player.board_position)
            
            # if not player.is_valid_player:
            #     XXX.reset_property(game_board.board, player)
            
            print('Propert has owner: ', game_board.board[player.board_position].return_property())
            print('Player money before: ', player.money)
            if game_board.board[player.board_position].return_property() != None:
                game_board.board[player.board_position].pay_rent_property(player=player, owner=game_board.board[player.board_position].owner)
            else:
                game_board.board[player.board_position].buy_property(player=player)
                print('New owner of property, player id: ', game_board.board[player.board_position].return_property().id)
            print('Player money after: ', player.money)
