class DART_BOARD:
    def __init__(self, type):
        self.board = [(i + 1) for i in range(20)]
        self.board.append('Bull')
        self.type = type
    
    def BullCout(self, throws):
        points_total = 0
        
        
    def PracticeDict(self, pracType):
        self.board
        if pracType == 'Doubles':
            pass
        elif pracType == 'Triples':
            pass  
        
        # while throws > 0:
        #     print('What did you hit? (0-2)?')
        #     turnHit = int(input())
        #     points_total += turnHit
        #     throws -= 1
            
        
def menu():
    pass

db = DART_BOARD('Bulls')
db.BullCount(int(input('How many darts are you throwing for Bull?   ')))