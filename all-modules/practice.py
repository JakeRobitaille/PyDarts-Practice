class DART_BOARD:
    def __init__(self, type):
        self.board = [(i + 1) for i in range(20)]
        self.board.append('Bull')
        self.type = type


class BULLS:
    def __init__(self):
        pass
     
    def BullCount(self):
        global throws
        global points_total
        points_total = 0
        throws = int(input('How many darts would you like to throw for bulls?   '))
        throwCount = throws
        
        while throwCount > 0:
            print('What did you hit? (0-2)?')
            turnHit = int(input())
            points_total += turnHit
            throwCount -= 1
        return points_total 
        
    def practice_bulls(self):
        self.BullCount()
        print(f'You got a total of {points_total} point(s) out of {throws} darts')

class DUB_TRIP(DART_BOARD):
    def __init__(self):
        super().__init__(self, type)
            
    def PracticeDict(self, pracType):
        self.board
        if pracType == 'Doubles':
            pass
        elif pracType == 'Triples':
            pass  


def main():
    pass

b = BULLS()
b.practice_bulls()