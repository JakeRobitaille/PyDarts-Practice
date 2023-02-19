import random

# Set up class to keep track of how many bulls to throw for and how many points you got
class BULLS:
    # Initializes trackers for misses, singles, doubles and total points earned
    def __init__(self):
        self.total_points = 0
        self.throws = 0
        self.miss = 0
        self.single = 0
        self.double = 0
    
    
    def Bull_Count(self):
        # Asks user to input how many darts will be thrown
        self.throws = int(input('How many darts would you like to throw for bulls?   -----> '))
        countDown = self.throws
        
        # User inputs what happened when throwing and trackers are updated accordingly
        while countDown > 0:
            print('What did you hit? (0-2)?')
            turnHit = int(input())
            if turnHit == 0:
                print('You Missed')
                self.miss += 1
            elif turnHit == 1:
                print('You hit a Single Bull')
                self.single += 1
            elif turnHit == 2:
                print('You hit a Double Bull')
                self.double += 1
            else:
                print('That is not a valid entry, try again.')
                continue    
            self.total_points += turnHit
            countDown -= 1
            print(f'{countDown} throws left... \n')
    
    # This calls Bull_Count() and outputs data for the user    
    def practice_bulls(self):
        self.Bull_Count()
        print(f'''You got a total of:
    - {self.total_points} point(s) out of {self.throws * 2} possible points
    - {self.single + self.double} Hits out of {self.throws} Darts thrown
        + {self.single} Single(s), {self.double} Double(s) and {self.miss} Misses
    - About {int(((self.single + self.double)/self.throws)*100)}% Hit rate''')

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
                answer = input(f'Did you hit the {type} {target}? Y / N   -----> ')                
                if answer == 'n' or answer == 'N':
                    print(f'You have thrown {throwCounter} darts \n')
                    throwCounter += 1
                elif answer == 'y' or answer == 'Y':
                    print(f'You got the {target} in {throwCounter} dart(s) \n')
                    hit = True
                else:
                    print('That is not a valid answer, try again: \n')
                
        return throwCounter   
    
    # Sets up the target number and darts thrown as key : value pairs in a dictionary            
    def dart_track(self, type):
        DARTBOARD = self.dart_board()
        turns_taken = {}
        
        for num in DARTBOARD:
            turns_taken[num] = self.is_hit(type, num)

        if type == 'triple':
            turns_taken.pop('Bull')
          
        return turns_taken

# Set up class to output a random number between 2-170 with input to show user how many points they have left
class rand_out:
    def __init__(self):
        # Sets up lists with all out possibilities with 3 or less darts 
        self.this_out = None
        self.this_hit = None
        self.lowEven = [i for i in range(2, 41) if i % 2 == 0]
        self.lowOdd = [i for i in range(3, 42) if i % 2 == 1]
        self.midEven = [i for i in range(42, 61) if i % 2 == 0]
        self.midOdd = [i for i in range(43, 60) if i % 2 == 1]
        self.highOut = [i for i in range(61, 99)]
        self.higherOut = [i for i in range(99, 119)]
        self.crazyOut = [i for i in range(119, 161) if i != 159]
        for i in range(161, 171, 3):
            self.crazyOut.append(i) 
    
    # Chooses a random number from the chosen list and outputs that number
    def Num_Output(self, outList):
        self.this_out = random.choice(outList)
        print(f'Your random out is: {self.this_out}')
    
    # Player will need to out in three darts or less
    def three_out(self):
        # Sets up which number sets to choose between
        roll = random.randint(0, 34)
        if roll == 0:
            self.Num_Output(self.crazyOut)
        elif roll > 0 and roll <= 3:
            self.Num_Output(self.higherOut)
        elif roll > 3 and roll <= 8:
            self.Num_Output(self.lowEven)
        elif roll > 8 and roll <= 12:
            self.Num_Output(self.highOut)
        elif roll > 12 and roll <= 19:
            self.Num_Output(self.midOdd)
        elif roll > 19 and roll <= 27:
            self.Num_Output(self.midEven)
        else:
            self.Num_Output(self.lowOdd)
        
        # Sets up tracker for points left after something is hit
        outTracker = self.this_out
        
        # Three darts to get something down
        for i in range(3):
            print(f'Turn {i + 1}:')
            self.this_hit = int(input('How many points did you hit?   -----> '))
            outTracker -= self.this_hit
            
            if outTracker == 0:
                print('Congrats, you got your out in 3 darts or less!')
                break
            else:
                print(f'You have {outTracker} points left \n')
                
        if outTracker > 0:
            print('You were unable to out in 3 darts')
            
    def until_out(self):
        roll = random.randint(0, 34)
        if roll == 0:
            self.Num_Output(self.crazyOut)
        elif roll > 0 and roll <= 3:
            self.Num_Output(self.higherOut)
        elif roll > 3 and roll <= 8:
            self.Num_Output(self.lowEven)
        elif roll > 8 and roll <= 12:
            self.Num_Output(self.highOut)
        elif roll > 12 and roll <= 19:
            self.Num_Output(self.midOdd)
        elif roll > 19 and roll <= 27:
            self.Num_Output(self.midEven)
        else:
            self.Num_Output(self.lowOdd)
            
        
def main():
    pass 

# dd = DUB_TRIP()
# game_1 = dd.dart_track('double')
# print(game_1)

# db = BULLS()
# game_2 = db.practice_bulls()

ro = rand_out()
ro.three_out()