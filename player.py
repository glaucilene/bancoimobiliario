class Player():

    def __init__(self, money, board_position, id, property = None):
        self.money = money
        self.property = property
        self.board_position = board_position
        self.id = id
    
    def is_valid_player(self, player):
        if player.money < 0:
            return False