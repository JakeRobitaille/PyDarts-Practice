import datetime

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
        try:
            self.throws = int(input('How many darts would you like to throw for bulls?   -----> '))
        except:
            print('A value is needed to continue...\n')
            self.Bull_Count()
        else:
            if self.throws == 0:
                print('Sorry, you have chosen to throw 0 darts. Try again...\n')
                self.Bull_Count()
            countDown = self.throws

        # User inputs what happened when throwing and trackers are updated accordingly
        while countDown > 0:
            print(f'\n{countDown} throws left... ')
            
            try:
                print('''What did you hit? -----> 
0 - Miss | 1 - Single | 2 - Double''')
                answer = int(input())
            except:
                print('\nThat is not a valid entry, try again.\n')
            else:
                match answer:
                    case 0:
                        print('You Missed')
                        self.miss += 1
                    case 1:
                        print('You hit a Single Bull')
                        self.single += 1
                    case 2:
                        print('You hit a Double Bull')
                        self.double += 1    
                    case _:
                        print("You must choose a number from 0 to 2...\n")
                        answer = 0
                        countDown += 1      
                self.total_points += answer
                countDown -= 1  
    
    # This calls Bull_Count() and outputs data for the user    
    def practice_bulls(self):
        self.Bull_Count()
        date = f'{datetime.date.today()}'
        gameInfo = {
            'Darts Thrown': self.throws, 
            'Darts Hit': self.single + self.double, 
            'Singles': self.single, 
            'Doubles': self.double, 
            'Misses': self.miss, 
            'Average Hit %': f'{int(((self.single + self.double)/self.throws)*100)}%', 
            'Points Out of Total': f'{self.total_points}/{self.throws * 2}', 
            'Date': date
        }
        
        print(f'''\nYou got {self.total_points} point(s) out of {self.throws * 2} possible points
{self.single + self.double} Total hits out of {self.throws} Darts thrown
{self.single} Single(s) hit 
{self.double} Double(s) hit 
{self.miss} Misses
About {int(((self.single + self.double)/self.throws)*100)}% Hit rate''')
        
        print('\n------ PRACTICE SAVED TO HISTORY ------\n')
        return gameInfo