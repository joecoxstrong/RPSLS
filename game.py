
from ai import AI 
from human import Human

class Game():
    def __init__(self):
        self.human = Human()
        self.ai = AI()

    def run_game(self):
        pass


    def choose_gesture(self):
        choose_index = int(input(f'{self.name}, select a gesture. '))
        return choose_index


