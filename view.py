#Jogo da Forca
from game import Game

class View(Game):
    
    def __init__(self):
        Game.__init__(self)
        
        
    
    def view(self):
        print('\n-----------------Welcome to the Game-----------------\n')
        print('Play or Settings\n')
        print(' 1-Play')
        print(' 2-Settings\n')
        while True:
            try:
                p_s=int(input('Type the number: '))
                if p_s == 1 or p_s == 2:
                    break
                else:
                    print('Incorrect number!')
            except:
                print('Type just numbers.')
        if p_s == 1:
            print('\nPlay\n')
            while True:
                self.play()
                try:
                    s_n=int(input('Do you want to play again?\n 1-Yes\n 2-No\nType a number: '))
                    if s_n == 2:
                      break
                    elif s_n == 1:
                        print('\nPlay\n')
                    else:
                        print('Incorrect Number!')
                except:
                    print('Type just numbers.')
            
        if p_s == 2:
            print('Set')









a=View()
a.view()
        