from player import Player
from ai import AI 
from human import Human

class Game():
    def __init__(self):
        self.human = Human(self)
        # self.ai = AI()
        pass

    def run_game(self):
        self.display_greeting()
        self.match()
        self.display_winner()


    def display_greeting(self):
        print("WELCOME! LIVE LONG AND PROSPER! LET'S GET READY TO PLAY 'ROCK, PAPER, SCISSORS, LIZARD, SPOCK'!")
        print("Here are the rules:\nScissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\n(and as it always has) Rock crushes Scissors")

    def match(self):
        pass

    def player_one_choice(self):
        pass

    def player_two_choice(self):
        pass

    def computer_choice(self):
        pass    

    # def human_choose_gesture(self):
    #     choose_index = int(input(f'{self.name}, select a gesture. '))
    #     return choose_index


    # def computer_choose_gesture(self):
    #     choose_index = random.randint(0,4)
    #     return choose_index



    def display_winner(self):
        pass

game = Game()
print(game.human.name)
        