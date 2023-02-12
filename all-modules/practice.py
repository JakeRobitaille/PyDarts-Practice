# Set up class to keep track of how many bulls to throw for and how many points you got
class BULLS:
    
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
        print(f'You got a total of {points_total} point(s) out of {throws} darts and {throws * 2} possible points')

# Set up class to keep track of darts thrown for either doubles or triples and how many shots it takes
class DUB_TRIP():
    
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
            answer = input(f'Did you hit the {type} {target}? Y / N \n')
            check = answer
            if check == 'n' or 'N':
                throwCounter += 1
            elif check== 'y' or 'Y':
                hit = True
            else:
                print('That is not a valid answer, try again:')
                
        return throwCounter
                
        
    
    # Sets up the target number and darts thrown as key : value pairs in a dictionary            
    def dart_track(self, type):
        DARTBOARD = self.dart_board()
        turns_taken = {}
        
        for num in DARTBOARD:
            turns_taken[num] = self.is_hit(type, num)
          
        return turns_taken
            

def main():
    pass

dd = DUB_TRIP()
print(dd.is_hit('triple', 1))