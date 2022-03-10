

class Set:
    def __init__(self):
        self.words=['house', 'horse', 'pencil', 'student', 'game', 'table', 'dog', 'cat', 'hospital', 'bacon', 'money', 'guitar']
        self.game=[]
    
    def createGame (self,word):
        game=[]
        for x in range(len(word)):
            game.append('-')
        self.game=game

    def addWord(self,word):
        self.words.append(word)

    def removeWord(self):
        for x in range(len(self.words)):
            print(' {}- {}'.format(x+1,self.words[x]))
        while True:
            try:
                num=int(input('Which word do you want to remove?'))
                if num <= len(self.words) and num >=0 :
                    break
                else:
                    print('Number incorrect!')
            except:
                print('Type just numbers!')
        self.words.pop(num-1)
