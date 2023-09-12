import random

from utils import set_board
class Wolf:
    def __init__(self) -> None:
        self.state = 'Выследить добычу'
        self.chance_to_kill = 0.5
        self.Yposition = 0
        self.Xposition = 0
    
    def plus_or_minus_position(self):
        self.Yposition += random.choice([-1, 0, 1])
        self.Xposition += random.choice([-1, 0, 1])
        self.Yposition = max(0, min(self.Yposition, 4))
        self.Xposition = max(0, min(self.Xposition, 4))
    
    def display_position(self):
        return (self.Xposition, self.Yposition)

    def is_rabbit_near(self, rabbits):
        for rabbit in rabbits:

            if abs(rabbit.Yposition - self.Yposition) <= 1 and abs(rabbit.Yposition - self.Yposition) <= 1:
                self.state = 'Атаковать добычу'
                
                if random.random() < self.chance_to_kill:
                    print('Волк успешно атаковал зайца')
                    self.state = 'Бежать домой'
                    return True
                else:
                
                    print('Волк промахнулся')
            else:
                break
                

    
    def start(self, rabbits):
        is_win = False
        while not is_win:       
            set_board(self, rabbits)
            print('\nКонец хода\n')
            self.plus_or_minus_position()
            if self.is_rabbit_near(rabbits):
                if_win = True
                
                

                break
        
        set_board(self, rabbits)