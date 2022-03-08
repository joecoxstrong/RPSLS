
from ai import AI 
from human import Human
import time

class Game():
    def __init__(self):
        self.human = Human()
        self.ai = AI()
        self.player_one_choice=0
        self.player_two_choice=0
        self.computer_choice=0
        

    def run_game(self):
        self.display_greeting()
        self.game_choice()
        self.display_winner()
        

    def display_greeting(self):
        print("WELCOME! LIVE LONG AND PROSPER! LET'S GET READY TO PLAY 'ROCK, PAPER, SCISSORS, LIZARD, SPOCK'!")
        time.sleep(1)
        print('Here are the rules:\n')
        time.sleep(1)
        print('Scissors cuts Paper\n')
        time.sleep(1)
        print('Paper covers Rock\n') 
        time.sleep(1)
        print('Rock crushes Lizard\n')
        time.sleep(1)
        print('Lizard poisons Spock\n')
        time.sleep(1)
        print('Spock smashes Scissors\n')
        time.sleep(1)
        print('Scissors decapitates Lizard\n')
        time.sleep(1)
        print('Lizard eats Paper\n')
        time.sleep(1)
        print('Paper disproves Spock\n')
        time.sleep(1)
        print('Spock vaporizes Rock\n')
        time.sleep(1)
        print('(and as it always has) Rock crushes Scissors\n')
        time.sleep(1)
    def game_choice(self):
        while True:
            try:    
                game_type = int(input('Which game would you like to play? For Human vs Human, Press (1), for Human vs Computer, Press (2): '))
            except ValueError:
                print('not a valid selection please try again')
                continue

            if game_type == 2 :
                print('You selected to play against the Computer.')
                self.computer_game()
                break
            elif game_type == 1:
                print('You selected Human vs Human.')
                self.human_game()
                break
            else:  
                print('Sorry, only 1 or 2 please') 
        

    def human_game(self):
        
        self.player01 = Human() 
        player_01 = self.player01.create_players()
        
        self.player02 = Human()
        player_02 = self.player02.create_players()
        self.player01.name = player_01
        self.player02.name = player_02
        print(f'(0)  {self.player01.gestures[0]}   (1) {self.player01.gestures[1]}  (2) {self.player01.gestures[2]} (3)  {self.player01.gestures[3]}     (4) {self.player01.gestures[4]} ')
        while self.player02.score != 2 and self.player01.score != 2:
            comp_player1 = self.human.choose_gesture()
            comp_player2 = self.human.choose_gesture()
            self.compare_gestures(comp_player1, comp_player2)
            

    def computer_game(self):
        
        self.player01 = Human() 
        player_01 = self.player01.create_players()
        
        
        self.player02 = AI()
        self.player01.name = player_01
        print(f'(0)  {self.player01.gestures[0]}   (1) {self.player01.gestures[1]}  (2) {self.player01.gestures[2]} (3)  {self.player01.gestures[3]}     (4) {self.player01.gestures[4]} ')
        while self.player02.score != 2 and self.player01.score != 2:
            comp_player = self.human.choose_gesture()
            comp_random = self.ai.ai_gesture()
            self.compare_gestures(comp_player, comp_random)
            print(self.player01.score)
            print(self.player02.score)
    

    def compare_gestures(self,gesture_01,gesture_02):
        gesture_a = self.player01.gestures[gesture_01]
        gesture_b = self.player02.gestures[gesture_02]
        print(f'{self.player01.name} chooses {gesture_a}')
        time.sleep(2)
        print(f'{self.player02.name} chooses {gesture_b}')
        time.sleep(2)
        
        if gesture_b == gesture_a:
            print('It\'s a tie! Please try again!\n')
            self.player01.score += 0       
            
        elif 'Rock' in gesture_a:
            if 'Paper' in gesture_b: 
                print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                time.sleep(2)
                self.player02.score +=1
            elif 'Spock' in gesture_b:
                print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                time.sleep(2)
                self.player02.score +=1
            
            else:
                print(f'{gesture_a} beats {gesture_b}, {self.player01.name} wins!\n')
                time.sleep(2)
                self.player01.score +=1

        elif 'Paper' in gesture_a:
            if 'Lizard' in gesture_b: 
                print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                time.sleep(2)
                self.player02.score +=1

            elif 'Scissor' in gesture_b:
                print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                time.sleep(2)
                self.player02.score +=1

            else:
                print(f'{gesture_a} beats {gesture_b}, {self.player01.name} wins!\n')
                time.sleep(2)
                self.player01.score +=1

        elif 'Scissor' in gesture_a:
            if 'Rock' in gesture_b: 
                print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                time.sleep(2)
                self.player02.score +=1

            elif 'Spock' in gesture_b:
                print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                time.sleep(2)
                self.player02.score +=1

            else:
                print(f'{gesture_a} beats {gesture_b}, {self.player01.name} wins!\n')
                time.sleep(2)
                self.player01.score +=1

        elif 'Lizard' in gesture_a:
                if 'Rock' in gesture_b: 
                    print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                    time.sleep(2)
                    self.player02.score +=1

                elif 'Scissor' in gesture_b:
                    print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                    time.sleep(2)
                    self.player02.score =+1
                else:
                    print(f'{gesture_a} beats {gesture_b}, {self.player01.name} wins!\n')
                    time.sleep(2)
                    self.player01.score +=1

        elif 'Spock' in gesture_a:
                if 'Paper' in gesture_b: 
                    print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                    time.sleep(2)
                    self.player02.score +=1

                elif 'Lizard' in gesture_b:
                    print(f'{gesture_b} beats {gesture_a}, {self.player02.name} wins!\n')
                    time.sleep(2)
                    self.player02.score +=1

                else:
                    print(f'{gesture_a} beats {gesture_b}, {self.player01.name} wins!\n')
                    time.sleep(2)
                    self.player01.score +=1
  


    def display_winner(self):
        if self.player01.score == 2:
            print(f'{self.player01.name} is the winner!!!!!\n')
            
        else: 
            print(f'{self.player02.name} is the winner!!!!!\n') 
            
            

