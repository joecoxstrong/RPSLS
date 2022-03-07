
from player import Player
import random


class AI(Player):
    def __init__(self, name):
        super().__init__(name)
        self.score = 0
        self.name = 'Computer'

    def choose_gesture(self):
        choose_index = random.randint(0,4)
        return choose_index
        # self.gesture = ['Rock','Paper','Scissor','Lizard','Spock']


ai = AI(Player)
random_number = ai.choose_gesture()
print(ai.gesture[random_number])
# print(gesture[self.chosen_gesture])