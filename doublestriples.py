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
    def dart_track(self, type, file):
        DARTBOARD = self.dart_board()
        turns_taken = []
        numberPrint = 1
        
        for num in DARTBOARD:
            turns_taken.append(self.is_hit(type, num))

        if type == 'triple':
            turns_taken.pop()
         
        for i in turns_taken:
            if numberPrint == 21:
                numberPrint = 'Bulls'
                print(f'{type} {str(numberPrint)}: {i} Throw(s)')
            else:  
                print(f'{type} {str(numberPrint)}: {i} Throw(s)')
                numberPrint += 1
              
        for i in turns_taken:
            readwrite.writeTo(file, f'{i}, ') 
        readwrite.writeTo(file, f'{datetime.date.today()}\n')
        print('\n------ PRACTICE SAVED TO HISTORY ------\n')
