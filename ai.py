import random

from player import Player



class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = 'Computer'

    def ai_gesture(self):
        random_gesture = random.randint(0,4)
        return random_gesture
        



