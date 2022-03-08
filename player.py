#Parrent file

from unicodedata import name


class Player():
    def __init__(self):
        self.name = ''
        self.gestures = ['Rock', 'Paper','Scissor','Lizard', 'Spock']
        self.chosen_gesture = ''
        self.score = 0

    def choose_gesture(self):
        
        while True:
            try:    
                chosen_gesture = int(input('Enter your gesture: '))
            except ValueError:
                print('not a valid selection please try again')
                continue

            if chosen_gesture >= 5 :
                print('Invalid Selection. Try Again.')
                
            # elif game_type == 1:
            #     print('You selected Human vs Human.')
            #     self.human_game()
            #     break
            else:  
                # self.computer_game()
        
                return chosen_gesture
       
    