# Class Human:
#   def __init__ (self, gesture):
#     self.name = name
#     self.gesture = gesture

from player import Player



class Human(Player):
    def __init__(self,name):
        super().__init__(name)
        self.score = 0
        self.name = input('Player, enter your name: ')

  
        


human = Human(Player)
print(human.name)
# chosen_number = human.choose_gesture()
# print(human.gesture[chosen_number])