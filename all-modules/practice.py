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
        self.roll = None
        self.lowEven = [i for i in range(2, 41) if i % 2 == 0]
        self.lowOdd = [i for i in range(3, 42) if i % 2 == 1]
        self.midEven = [i for i in range(42, 61) if i % 2 == 0]
        self.midOdd = [i for i in range(43, 60) if i % 2 == 1]
        self.highOut = [i for i in range(61, 99)]
        self.higherOut = [i for i in range(99, 119)]
        self.crazyOut = [i for i in range(119, 171) if i != 159 or i != 162 or i != 163 or i != 165 or i != 166 or i != 168 or i != 169] 
    
    # Sets up which number sets to chose between
    def Prob_Roll(self):
        return random.randint(0, 34)
    
    def your_out(self):
        roll = self.Prob_Roll()
        print(roll)
        

def main():
    pass 

# dd = DUB_TRIP()
# game_1 = dd.dart_track('triple')
# print(game_1)

db = BULLS()
game_2 = db.practice_bulls()

# ro = rand_out()
# print(f'''{ro.lowEven}
#       {ro.lowOdd}
#       {ro.midEven}
#       {ro.midOdd}
#       {ro.highOut}
#       {ro.higherOut}
#       {ro.crazyOut}
#       ''')