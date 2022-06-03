from property import Property

class GameBoard():

    def __init__(self, number_positions):
        self.number_positions = number_positions
        self.board = []
    
    def create_board(self):
        for i in range(self.number_positions):
            self.board.append(Property(sale_value=10, rent_value=5))