

from player import Player



class Human(Player):
    def __init__(self,name):
        super().__init__(name)
        self.score = 0
        self.name = input('Player, enter your name: ')

  
        