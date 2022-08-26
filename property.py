class Property():

    def __init__(self, sale_value, rent_value, owner=None):
        self.sale_value = sale_value
        self.rent_value = rent_value
        self.owner = owner
    
    def buy_property(self, player):
        if player.money >= self.sale_value:
            self.owner = player
            player.money = player.money - self.sale_value
            # TODO: Conferir a lista de propriedades no player
            print('Self: ', self)
            if player.property:
                player.property.append(self)
            else:
                player.property = [self]
        else:
            print("No money to buy property")

    def pay_rent_property(self, player, owner):
        player.money = player.money - self.rent_value
        owner.money = owner.money + self.rent_value

    def return_property(self):
        return self.owner

    def reset_property(self, list_property, player):
        for property in list_property:
            pass
