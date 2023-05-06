import readwrite
import datetime

# Set up class to keep track of darts thrown for either doubles or triples and how many shots it takes
class DUB_TRIP:           
    # This is to set up the numbers associated with a dart board
    def dart_board(self):
        darts = [str(i + 1) for i in range(20)]
        darts.append('Bull')
        return darts
   
    # Checks to see if target is hit and if not repeats until it is and returns the amounnt of throws        
    def is_hit(self, type, target):
        throwCounter = 1
        hit = False
        
        while hit == False:
            # Bull has no triple so if the practice type is 'triple', auto skips bulls
            if target == 'Bull' and type == 'triple':
                hit = True
            else:
                answer = input(f'Did you hit the {type} {target}?\n 1 for Y | 2 for N   -----> ')
                if answer == '2':
                    print(f'You have thrown {throwCounter} darts \n')
                    throwCounter += 1
                elif answer == '1':
                    print(f'You got the {type} {target} in {throwCounter} dart(s) \n')
                    hit = True
                else:
                    print('That is not a valid answer, try again \n')
                
        return throwCounter   
    
    # Sets up the target number and darts thrown as key : value pairs in a dictionary            
    def dart_track(self, type):
        DARTBOARD = self.dart_board()
        if type == 'triple':
            DARTBOARD.pop()
        gameInfo = {}
        date = f'{datetime.date.today()}'
        
        for num in DARTBOARD:
            gameInfo.update({num : self.is_hit(type, num)})
        gameInfo.update({'Date' : date})
        
        print('Your Stats:')
        for key in gameInfo:
            print(f'{key} : {gameInfo[key]}')

        print('\n------ PRACTICE SAVED TO HISTORY ------\n')
        return gameInfo
