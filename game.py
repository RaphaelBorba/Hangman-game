from random import randint
from set import Set



class Game(Set):
    
    def __init__(self):
        Set.__init__(self)
        self.win_or_lose=''
    
    def play(self):
        trys=5
        x=randint(0,(len(self.words)-1))
        word=self.words[x]
        self.createGame(self.words[x])
        
        answer=list(word)
        print(self.game)
        print(answer)
        while True:
            if answer == self.game:
                print('\nYou Win!\n')
                self.win_or_lose='win'
                break
            char=input('Inform one char: ')
            if char in answer:
                for y in range(len(answer)):
                    if char == answer[y-1]:
                        self.game[y-1]=answer[y-1]
                        print(self.game)
            else:
                trys-=1
                print('Less one try {}'.format(trys))
                if trys == 0:
                    print('\nYou lose!\n')
                    self.win_or_lose='lose'
                    break



