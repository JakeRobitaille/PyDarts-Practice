import random
import datetime

# Set up class to output a random number between 2-170 with input to show user how many points they have left
class rand_out:
    def __init__(self):
        # Sets up lists with all out possibilities with 3 or less darts 
        self.gameType = None
        self.this_out = None
        self.this_hit = None
        self.outInThree = False
        self.dartsToOut = None
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
        print('-----------------------')
    
    # Player will need to out in three darts or less
    def Out_Choice(self):
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
    
    # Player throws three darts to try and out    
    def three_out(self): 
        self.gameType = 'Three Darts To Close' 
        self.Out_Choice()
        # Sets up tracker for points left after something is hit
        outTracker = self.this_out
        dartsTaken = 1
        i = 3
        # Three darts to get out
        while i > 0:
            print(f'\nDart {dartsTaken}:')
            
            try:
                self.this_hit = int(input('\nHow many points did you hit?   -----> '))
            except:
                print('A value is needed to continue...\n')
            else:
                outTracker -= self.this_hit
                i -= 1
                if outTracker != 0:
                    dartsTaken += 1
            
            if outTracker == 0:
                print('\nCongrats, you got your out in 3 darts or less!')
                self.dartsToOut = i + 1
                break
            else:
                print(f'\nYou have {outTracker} points left \n')
                
        if outTracker > 0:
            print('\nYou were unable to out in 3 darts')
        else:
            self.outInThree = True
            
        return self.writeOut()
     
    # Player throws until they get an out  
    def until_out(self):
        self.gameType = 'Throw Until Close'
        self.Out_Choice()
        outTracker = self.this_out
        dartsTaken = 1
        
        while(outTracker > 0):
            print(f'\nDart {dartsTaken}:')
            
            try:
                self.this_hit = int(input('How many points did you hit?   -----> '))
            except:
                print('A value is needed to continue...\n')
            else:
                outTracker -= self.this_hit
                if outTracker != 0:
                    dartsTaken += 1
            
            if outTracker == 0:
                print(f'\nYou got your out in {dartsTaken} darts')
                self.dartsToOut = dartsTaken
                if dartsTaken <= 3:
                    self.outInThree = True
                break
            else:
                print(f'\nYou have {outTracker} points left \n')
        
        return self.writeOut()
    
                
    def writeOut(self):
        date = f'{datetime.date.today()}'
        
        print(f'''\nRandom Number: {self.this_out} 
Able to out in 3 darts?: {str(self.outInThree)} 
Darts thrown to out: {self.didOut()}\n''')
        
        gameInfo = {
            'Game Type' : self.gameType,
            'Random Out' : self.this_out,
            'Out in 3?' : str(self.outInThree),
            'Darts Thrown' : self.didOut(),
            'Date' : date
        }

        print('\n------ PRACTICE SAVED TO HISTORY ------\n')
        return gameInfo
        
    
    def didOut(self):
        if self.dartsToOut:
            return self.dartsToOut
        else:
            return 'N/A'