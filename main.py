from ctypes import sizeof
import random
# TODO: Item 74 (Tabuleiro), Verificar o Jogo da Lista Organizada (Turno)

class GameBoard():

    def __init__(self, number_positions):
        self.number_positions = number_positions
        self.board = []
    
    def create_board(self):
        for i in range(self.number_positions):
            self.board.append(Property(sale_value=10, rent_value=10))

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

    def __init__(self, money, board_position, id, property = None):
        self.money = money
        self.property = property
        self.board_position = board_position
        self.id = id


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

        list_position_players = self.sort_players()

        print(f'Players sequence: {list_position_players}')

        print('Teste turno')
        turn = Turns(number_turns=2)
        players = turn.player_create(list_position_players)

        # TODO: preparar while para simulação

        # turn.turn_control(players=players)


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
        
        print(players)
        for player in players:
            print(player.id)

        return players

    
    def turn_control(self, players, game_board):
        # (Na jogada 1000 jogador com maior saldo ganha) - critério desempate é ordem dos jogadores
        if self.turn == 1000:
            greater_balance = 0
            winner = None
            for player in players:
                if player.money > greater_balance:
                    greater_balance = player.money
                    winner = player
            print(f'O ganhador foi o jogador:{winner.id}')
        else:
            self.turn = self.turn + 1
            # TODO: poderia verificar se tem nova lista de jogadores - Checar onde por
            for player in players:
                die_result = random.randint(1, 6)
                if (player.board_position + die_result) > 20:
                    new_die = (player.board_position + die_result) - 20
                    player.board_position = new_die
                else:
                    player.board_position += die_result
                
                # TODO: Fazer teste da implementação
                if game_board.board[player.board_position].return_property() != None:
                    game_board.board[player.board_position].pay_rent_property(player=player, owner=game_board.board[player.board_position].owner)

    # def turns(self, list_players):
    #     turn_control = {}
    #     for player in list_players:
    #         turn_control = {player, self.turn}
    #     return None

if __name__ == '__main__':
    Simulator(number_players=4).run()
