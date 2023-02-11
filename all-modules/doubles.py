class DART_BOARD:
    def __init__(self, type):
        self.board = [(i + 1) for i in range(20)]
        self.board.append('Bull')
        self.type = type
    
    def double(self, throws):
        points_total = 0
        
        
    def practice_dict(self):
        self.board
        dartThrows = []    
        
        # while throws > 0:
        #     print('How many did you hit (0-2)?')
        #     turnHit = int(input())
        #     points_total += turnHit
        #     throws -= 1
            
        
def menu():
    pass

db = DART_BOARD('Bulls')
db.bullCount(int(input('How many darts are you throwing for Bull?   ')))