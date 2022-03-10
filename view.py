#Jogo da Forca
from game import Game

class View(Game):
    
    def __init__(self):
        Game.__init__(self)
        
        
    
    def view(self):
        print('\n-----------------Welcome to the Game-----------------\n')
        print('Play or Settings\n')
        print(' 1-Play')
        print(' 2-Settings')
        print(' 3-Exit\n')
        while True:
            try:
                p_s=int(input('Type the number: '))
                if p_s == 1 or p_s == 2 or p_s==3:
                    break
                else:
                    print('Incorrect number!')
            except:
                print('Type just numbers.')
        if p_s == 1:
            print('\nPlay\n')
            self.play()
            while True:
                try:
                    s_n=int(input('Do you wanna play again?\n 1-Yes\n 2-No\nType a number: '))
                    if s_n == 2:
                      break
                    elif s_n == 1:
                        print('\nPlay\n')
                        self.play()
                    else:
                        print('Incorrect Number!')
                except:
                    print('Type just numbers.')
            self.view()
        if p_s == 2:
            print('\nSettings\n')
            print('What do you wanna do?\n')
            print(' 1-Add a new word on the game.')
            print(' 2-Remove a word on the game.\n')
            while True:
                try:
                    ab=int(input('Type the number: '))
                    if ab == 1 or ab == 2:
                        break
                    else:
                        print('Incorrect number!')
                except:
                    print('Type just numbers.')
            if ab == 1:
                print('\nAdd Word!\n')
                new_word=input('Inform the new word: ')
                self.addWord(new_word)
                
            if ab == 2:
                print('\nRemove Word!\n')
                self.removeWord()
            self.view()
        if p_s == 3:
            print('\n!!!-GAME OVER-!!!\n')







a=View()
a.view()
        